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
 * The supported OrgObject types
 */
export enum OrgObjectTypes {
  OU = 'ou',
  ACCOUNT = 'account',
}

/**
 * The properties of an OU
 */
export interface OUProps {
  /**
   * The name of the OU
   */
  readonly name: string;
  /**
   * Whether or not to import an existing OU if the new OU is a duplicate. If this is false and the OU already exists an error will be thrown.
   *
   * @default false
   */
  readonly importOnDuplicate?: boolean;
  /**
    * Whether or not to merge an OU with a duplicate when an OU is moved between parent OUs.
    * If this is false and the OU already exists an error will be thrown.
    * If this is true and the OU already exists the accounts in the OU will be moved to the existing OU
    * and the duplicate, now empty, OU will be deleted.
    *
    * @default false
    */
  readonly allowMergeOnMove?: boolean;
  /**
    * Whether or not a missing OU should be recreated during an update.
    * If this is false and the OU does not exist an error will be thrown when you try to update it.
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
};

/**
 * The structure of an OrgObject
 */
export interface OrgObject {
  /**
   * The unique id of the OrgObject. This is used as the unique identifier when instantiating a construct object.
   * This is important for the CDK to be able to maintain a reference for the object when utilizing
   * the processOrgObj function rather then using the name property of an object which could change.
   * If the id changes the CDK treats this as a new construct and will create a new construct resource and
   * destroy the old one.
   *
   * Not strictly required but useful when using the processOrgObj function. If the id is not provided
   * the name property will be used as the id in processOrgObj.
   *
   * You can create a unique id however you like. A bash example is provided.
   * @example
   * echo "ou-$( echo $RANDOM | md5sum | head -c 8 )"
   */
  readonly id?: string;
  /**
   * The org object properties.
   */
  readonly properties: OUProps | AccountProps;
  /**
   * The type of the org object.
   */
  readonly type: OrgObjectTypes;
  /**
   * Other org objects that are children of this org object.
   */
  readonly children: OrgObject[];
}

/**
 * @function processOrgObj
 * Function to process an OrgObject and create the corresponding AWS resources
 *
 * @param {Construct} this The construct resources will be added to.
 * @param {custom_resources.Provider} provider The custom resource provider the custom resources will utilized to create the resources.
 * @param {OrgObject} obj The OrgObject to process.
 * @param {string | OrganizationOU} parent The parent of the OrgObject. This is either a string, like for the org root, or an OrganizationOU object from the same stack.
 */
export function processOrgObj(this: Construct, provider: custom_resources.Provider, obj: OrgObject, parent: string | OrganizationOU) {
  if (obj.type === OrgObjectTypes.OU) {
    const parentStr = parent instanceof OrganizationOU ? parent.resource.ref : parent;

    let props: OUProps = obj.properties;
    let id = obj.id ?? obj.properties.name;

    const ou = new OrganizationOU(this, id, {
      provider,
      parent: parentStr,
      name: props.name,
      importOnDuplicate: props.importOnDuplicate,
      allowMergeOnMove: props.allowMergeOnMove,
      allowRecreateOnUpdate: props.allowRecreateOnUpdate,
    });

    obj.children.forEach(child => {
      processOrgObj.call(this, provider, child, ou);
    });
  }
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
    const allowMergeOnMove = props.allowMergeOnMove ?? false;
    const allowRecreateOnUpdate = props.allowRecreateOnUpdate ?? false;

    const parentStr = props.parent instanceof OrganizationOU ? props.parent.resource.ref : props.parent;

    this.resource = new CustomResource(this, 'ou', {
      serviceToken: props.provider.serviceToken,
      properties: {
        Parent: parentStr,
        Name: props.name,
        ImportOnDuplicate: importOnDuplicate,
        AllowMergeOnMove: allowMergeOnMove,
        AllowRecreateOnUpdate: allowRecreateOnUpdate,
      },
    });

    this.resource.node.addDependency(props.provider);
    if (props.parent instanceof OrganizationOU) {
      this.resource.node.addDependency(props.parent);
    };
  }
}

// export interface OrganizationAccountProps {
//   /**
//    * The name of the account
//    */
//    readonly name: string;
//   /**
//    * The email for the account
//    */
//    readonly email: string;
//   /**
//   * The OU id for the account. This property is always preferred if id and name are both given. Defaults to the root
//   */
//    readonly ou_id?: string;
//   /**
//    * The OU name for the account. This property is ignored if the ou id is given.
//    */
//    readonly ou_name?: string;
// }

// export class OrganizationAccount extends Construct {
//   constructor(scope: Construct, id: string, props: OrganizationAccountProps) {
//     super(scope, id);

//     // code
//   }
// }
