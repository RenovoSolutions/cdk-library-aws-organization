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

export interface OrganizationOUProviderProps {
  /**
   * The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically
   */
  readonly role?: iam.IRole;
}

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

export interface OrganizationOUProps {
  /**
   * The name of the OU
   */
  readonly name: string;
  /**
   * The parent OU id
   */
  readonly parentId: string;
  /**
   * The provider to use for the custom resource that will create the OU. You can create a provider with the OrganizationOuProvider class
   */
  readonly provider: custom_resources.Provider;
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
}

export class OrganizationOU extends Construct {
  constructor(scope: Construct, id: string, props: OrganizationOUProps) {
    super(scope, id);

    const importOnDuplicate = props.importOnDuplicate ?? false;
    const allowMergeOnMove = props.allowMergeOnMove ?? false;
    const allowRecreateOnUpdate = props.allowRecreateOnUpdate ?? false;

    new CustomResource(this, 'ou', {
      serviceToken: props.provider.serviceToken,
      properties: {
        ParentId: props.parentId,
        Name: props.name,
        ImportOnDuplicate: importOnDuplicate,
        AllowMergeOnMove: allowMergeOnMove,
        AllowRecreateOnUpdate: allowRecreateOnUpdate,
      },
    });
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
