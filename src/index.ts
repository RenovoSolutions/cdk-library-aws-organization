import * as path from 'path';
import {
  custom_resources,
  aws_lambda as lambda,
  aws_iam as iam,
  CustomResource,
  aws_logs as logs,
  Duration,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

/**
 * The properties of an OU
 */
export interface OUProps {
  /**
   * The name of the OU
   */
  readonly name: string;
  /**
   * Whether or not to import an existing OU if the new OU is a duplicate.
   * If this is false and the OU already exists an error will be thrown.
   *
   * @default false
   */
  readonly importOnDuplicate?: boolean;
  /**
   * Whether or not a missing OU should be recreated during an update.
   * If this is false and the OU does not exist an error will be thrown when you try to update it.
   *
   * @default false
   */
  readonly allowRecreateOnUpdate?: boolean;
};

/**
 * The properties of an Account
 */
export interface AccountProps {
  /**
   * The name of the account
   */
  readonly name: string;
  /**
   * The email address of the account. Most be unique.
   */
  readonly email: string;
  /**
   * Whether or not to import an existing account if the new account is a duplicate.
   * If this is false and the account already exists an error will be thrown.
   *
   * @default false
   */
  readonly importOnDuplicate?: boolean;
  /**
   * Whether or not to allow this account to be moved between OUs. If importing is enabled
   * this will also allow imported accounts to be moved.
   *
   * @default false
   */
  readonly allowMove?: boolean;
  /**
   * Whether or not attempting to delete an account should raise an error.
   *
   * Accounts cannot be deleted programmatically, but they can be removed as a managed resource.
   * This property will allow you to control whether or not an error is thrown
   * when the stack wants to delete an account (orphan it) or if it should continue
   * silently.
   *
   * @see https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/
   *
   * @default false
   */
  readonly disableDelete?: boolean;
};

/**
 * The structure of an OrgObject
 */
export interface OUObject {
  /**
   * The unique id of the OUObject. This is used as the unique identifier when instantiating a construct object.
   * This is important for the CDK to be able to maintain a reference for the object when utilizing
   * the processOUObj function rather then using the name property of an object which could change.
   * If the id changes the CDK treats this as a new construct and will create a new construct resource and
   * destroy the old one.
   *
   * Not strictly required but useful when using the processOUObj function. If the id is not provided
   * the name property will be used as the id in processOUObj.
   *
   * You can create a unique id however you like. A bash example is provided.
   * @example
   * echo "ou-$( echo $RANDOM | md5sum | head -c 8 )"
   */
  readonly id?: string;
  /**
   * The OU object properties.
   */
  readonly properties: OUProps;
  /**
   * Accounts that belong to this OU
   */
  readonly accounts?: AccountProps[];
  /**
   * OUs that are children of this OU
   */
  readonly children: OUObject[];
}

/**
 * @function processOUObj
 * Function to process an OrgObject and create the corresponding AWS resources
 *
 * @param {Construct} this The construct resources will be added to.
 * @param {custom_resources.Provider} ouProvider The custom resource provider for managing OUs
 * @param {custom_resources.Provider} accountProvider The custom resource provider for managing accounts
 * @param {OUObject} obj The OrgObject to process.
 * @param {string | OrganizationOU} parent The parent of the OrgObject. This is either a string, like for the org root, or an OrganizationOU object from the same stack.
 */
export function processOUObj(
  this: Construct,
  ouProvider: custom_resources.Provider,
  accountProvider: custom_resources.Provider,
  obj: OUObject,
  parent: string | OrganizationOU,
) {
  const parentStr = parent instanceof OrganizationOU ? parent.resource.ref : parent;
  let id = obj.id ?? obj.properties.name;

  const ou = new OrganizationOU(this, id, {
    provider: ouProvider,
    parent: parentStr,
    name: obj.properties.name,
    importOnDuplicate: obj.properties.importOnDuplicate,
    allowRecreateOnUpdate: obj.properties.allowRecreateOnUpdate,
  });

  obj.accounts?.forEach((account) => {
    new OrganizationAccount(this, `${account.name}-${account.email.replace(/[^a-zA-Z ]/g, '')}`, {
      provider: accountProvider,
      parent: ou,
      name: account.name,
      email: account.email,
      importOnDuplicate: account.importOnDuplicate,
      allowMove: account.allowMove,
      disableDelete: account.disableDelete,
    });
  });

  obj.children.forEach(child => {
    processOUObj.call(this, ouProvider, accountProvider, child, ou);
  });
}

/**
 * The properties for the OU custom resource provider.
 */
export interface OrganizationOUProviderProps {
  /**
   * The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically
   */
  readonly role?: iam.IRole;
}

/**
 * The provider for OU custom resources
 *
 * This creates a lambda function that handles custom resource requests for creating/updating/deleting OUs.
 */
export class OrganizationOUProvider extends Construct {

  public readonly provider: custom_resources.Provider;

  constructor(scope: Construct, id: string, props: OrganizationOUProviderProps) {
    super(scope, id);

    let role: iam.IRole;

    if (!props.role) {
      role = new iam.Role(this, 'role', {
        assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      });

      let policy = new iam.ManagedPolicy(this, 'policy', {
        statements: [
          new iam.PolicyStatement({
            actions: [
              'organizations:UpdateOrganizationalUnit',
              'organizations:DeleteOrganizationalUnit',
              'organizations:ListOrganizationalUnitsForParent',
              'organizations:CreateOrganizationalUnit',
            ],
            resources: ['*'],
          }),
        ],
      });

      role.addManagedPolicy(policy);
      role.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole'));
    } else {
      role = props.role;
    }

    const handlersPath = path.join(__dirname, '../handlers');

    const onEvent = new lambda.Function(this, 'handler', {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset(handlersPath + '/ou'),
      handler: 'index.on_event',
      timeout: Duration.seconds(10),
      role,
    });

    this.provider = new custom_resources.Provider(this, 'provider', {
      onEventHandler: onEvent,
      logRetention: logs.RetentionDays.ONE_DAY,
    });
  }
}

/**
 * The properties of an OrganizationOU custom resource.
 */
export interface OUResourceProps extends OUProps {
  /**
   * The parent OU id
   */
  readonly parent: string | OrganizationOU;
  /**
   * The provider to use for the custom resource that will create the OU. You can create a provider with the OrganizationOuProvider class
   */
  readonly provider: custom_resources.Provider;
}

/**
 * The construct to create or update an Organization OU
 *
 * This relies on the custom resource provider OrganizationOUProvider.
*/
export class OrganizationOU extends Construct {

  public readonly resource: CustomResource;

  constructor(scope: Construct, id: string, props: OUResourceProps) {
    super(scope, id);

    const importOnDuplicate = props.importOnDuplicate ?? false;
    const allowRecreateOnUpdate = props.allowRecreateOnUpdate ?? false;

    const parentStr = props.parent instanceof OrganizationOU ? props.parent.resource.ref : props.parent;

    this.resource = new CustomResource(this, 'ou', {
      serviceToken: props.provider.serviceToken,
      properties: {
        Parent: parentStr,
        Name: props.name,
        ImportOnDuplicate: importOnDuplicate,
        AllowRecreateOnUpdate: allowRecreateOnUpdate,
      },
    });

    this.resource.node.addDependency(props.provider);
    if (props.parent instanceof OrganizationOU) {
      this.resource.node.addDependency(props.parent);
    };
  }
}

/**
 * The properties for the account custom resource provider.
 */
export interface OrganizationAccountProviderProps {
  /**
   * The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically
   */
  readonly role?: iam.IRole;
}

/**
 * The provider for account custom resources
 *
 * This creates a lambda function that handles custom resource requests for creating/updating accounts.
 */
export class OrganizationAccountProvider extends Construct {

  public readonly provider: custom_resources.Provider;

  constructor(scope: Construct, id: string, props: OrganizationOUProviderProps) {
    super(scope, id);

    let role: iam.IRole;

    if (!props.role) {
      role = new iam.Role(this, 'role', {
        assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      });

      let policy = new iam.ManagedPolicy(this, 'policy', {
        statements: [
          new iam.PolicyStatement({
            actions: [
              'organizations:ListOrganizationalUnitsForParent',
              'organizations:ListAccountsForParent',
              'organizations:ListRoots',
              'organizations:MoveAccount',
              'organizations:DescribeAccount',
              'organizations:DescribeCreateAccountStatus',
              'organizations:CreateAccount',
            ],
            resources: ['*'],
          }),
        ],
      });

      role.addManagedPolicy(policy);
      role.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole'));
    } else {
      role = props.role;
    }

    const handlersPath = path.join(__dirname, '../handlers');

    const onEvent = new lambda.Function(this, 'handler', {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset(handlersPath + '/account'),
      handler: 'index.on_event',
      timeout: Duration.seconds(300),
      role,
    });

    this.provider = new custom_resources.Provider(this, 'provider', {
      onEventHandler: onEvent,
      logRetention: logs.RetentionDays.ONE_DAY,
    });
  }
}

/**
 * The properties of an OrganizationAccount custom resource.
 */
export interface AccountResourceProps extends AccountProps {
  /**
   * The parent OU id
   */
  readonly parent: string | OrganizationOU;
  /**
   * The provider to use for the custom resource that will create the OU. You can create a provider with the OrganizationOuProvider class
   */
  readonly provider: custom_resources.Provider;
}

/**
 * The construct to create or update an Organization account
 *
 * This relies on the custom resource provider OrganizationAccountProvider.
*/
export class OrganizationAccount extends Construct {

  public readonly resource: CustomResource;

  constructor(scope: Construct, id: string, props: AccountResourceProps) {
    super(scope, id);

    const importOnDuplicate = props.importOnDuplicate ?? false;
    const allowMove = props.allowMove ?? false;
    const disableDelete = props.disableDelete ?? false;

    const parentStr = props.parent instanceof OrganizationOU ? props.parent.resource.ref : props.parent;

    this.resource = new CustomResource(this, 'ou', {
      serviceToken: props.provider.serviceToken,
      properties: {
        Parent: parentStr,
        Name: props.name,
        Email: props.email,
        ImportOnDuplicate: importOnDuplicate,
        AllowMove: allowMove,
        DisableDelete: disableDelete,
      },
    });

    this.resource.node.addDependency(props.provider);
    if (props.parent instanceof OrganizationOU) {
      this.resource.node.addDependency(props.parent);
    };
  }
}
