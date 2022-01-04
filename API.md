# API Reference <a name="API Reference"></a>

## Constructs <a name="Constructs"></a>

### OrganizationAccount <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount"></a>

The construct to create or update an Organization account.

This relies on the custom resource provider OrganizationAccountProvider.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.Initializer"></a>

```typescript
import { OrganizationAccount } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationAccount(scope: Construct, id: string, props: AccountResourceProps)
```

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.parameter.scope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.parameter.id"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.parameter.props"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.AccountResourceProps`](#@renovosolutions/cdk-library-aws-organization.AccountResourceProps)

---



#### Properties <a name="Properties"></a>

##### `resource`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.property.resource"></a>

```typescript
public readonly resource: CustomResource;
```

- *Type:* [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource)

---


### OrganizationAccountProvider <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider"></a>

The provider for account custom resources.

This creates a lambda function that handles custom resource requests for creating/updating accounts.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.Initializer"></a>

```typescript
import { OrganizationAccountProvider } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationAccountProvider(scope: Construct, id: string, props: OrganizationOUProviderProps)
```

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.parameter.scope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.parameter.id"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.parameter.props"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps`](#@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps)

---



#### Properties <a name="Properties"></a>

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.property.provider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

---


### OrganizationOU <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU"></a>

The construct to create or update an Organization OU.

This relies on the custom resource provider OrganizationOUProvider.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.Initializer"></a>

```typescript
import { OrganizationOU } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationOU(scope: Construct, id: string, props: OUResourceProps)
```

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.scope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.id"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.props"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OUResourceProps`](#@renovosolutions/cdk-library-aws-organization.OUResourceProps)

---



#### Properties <a name="Properties"></a>

##### `resource`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.property.resource"></a>

```typescript
public readonly resource: CustomResource;
```

- *Type:* [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource)

---


### OrganizationOUProvider <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider"></a>

The provider for OU custom resources.

This creates a lambda function that handles custom resource requests for creating/updating/deleting OUs.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.Initializer"></a>

```typescript
import { OrganizationOUProvider } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationOUProvider(scope: Construct, id: string, props: OrganizationOUProviderProps)
```

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.parameter.scope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.parameter.id"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.parameter.props"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps`](#@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps)

---



#### Properties <a name="Properties"></a>

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.property.provider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

---


## Structs <a name="Structs"></a>

### AccountProps <a name="@renovosolutions/cdk-library-aws-organization.AccountProps"></a>

The properties of an Account.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { AccountProps } from '@renovosolutions/cdk-library-aws-organization'

const accountProps: AccountProps = { ... }
```

##### `email`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.email"></a>

```typescript
public readonly email: string;
```

- *Type:* `string`

The email address of the account.

Most be unique.

---

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.name"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the account.

---

##### `allowMove`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.allowMove"></a>

```typescript
public readonly allowMove: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to allow this account to be moved between OUs.

If importing is enabled
this will also allow imported accounts to be moved.

---

##### `disableDelete`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.disableDelete"></a>

```typescript
public readonly disableDelete: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not attempting to delete an account should raise an error.

Accounts cannot be deleted programmatically, but they can be removed as a managed resource.
This property will allow you to control whether or not an error is thrown
when the stack wants to delete an account (orphan it) or if it should continue
silently.

> https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.importOnDuplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing account if the new account is a duplicate.

If this is false and the account already exists an error will be thrown.

---

### AccountResourceProps <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps"></a>

The properties of an OrganizationAccount custom resource.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { AccountResourceProps } from '@renovosolutions/cdk-library-aws-organization'

const accountResourceProps: AccountResourceProps = { ... }
```

##### `email`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.email"></a>

```typescript
public readonly email: string;
```

- *Type:* `string`

The email address of the account.

Most be unique.

---

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.name"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the account.

---

##### `allowMove`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.allowMove"></a>

```typescript
public readonly allowMove: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to allow this account to be moved between OUs.

If importing is enabled
this will also allow imported accounts to be moved.

---

##### `disableDelete`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.disableDelete"></a>

```typescript
public readonly disableDelete: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not attempting to delete an account should raise an error.

Accounts cannot be deleted programmatically, but they can be removed as a managed resource.
This property will allow you to control whether or not an error is thrown
when the stack wants to delete an account (orphan it) or if it should continue
silently.

> https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.importOnDuplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing account if the new account is a duplicate.

If this is false and the account already exists an error will be thrown.

---

##### `parent`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.parent"></a>

```typescript
public readonly parent: string | OrganizationOU;
```

- *Type:* `string` | [`@renovosolutions/cdk-library-aws-organization.OrganizationOU`](#@renovosolutions/cdk-library-aws-organization.OrganizationOU)

The parent OU id.

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.provider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

The provider to use for the custom resource that will create the OU.

You can create a provider with the OrganizationOuProvider class

---

### OrganizationAccountProviderProps <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProviderProps"></a>

The properties for the account custom resource provider.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { OrganizationAccountProviderProps } from '@renovosolutions/cdk-library-aws-organization'

const organizationAccountProviderProps: OrganizationAccountProviderProps = { ... }
```

##### `role`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProviderProps.property.role"></a>

```typescript
public readonly role: IRole;
```

- *Type:* [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole)

The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically.

---

### OrganizationOUProviderProps <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps"></a>

The properties for the OU custom resource provider.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { OrganizationOUProviderProps } from '@renovosolutions/cdk-library-aws-organization'

const organizationOUProviderProps: OrganizationOUProviderProps = { ... }
```

##### `role`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps.property.role"></a>

```typescript
public readonly role: IRole;
```

- *Type:* [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole)

The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically.

---

### OUObject <a name="@renovosolutions/cdk-library-aws-organization.OUObject"></a>

The structure of an OrgObject.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { OUObject } from '@renovosolutions/cdk-library-aws-organization'

const oUObject: OUObject = { ... }
```

##### `children`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.children"></a>

```typescript
public readonly children: OUObject[];
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OUObject`](#@renovosolutions/cdk-library-aws-organization.OUObject)[]

OUs that are children of this OU.

---

##### `properties`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.properties"></a>

```typescript
public readonly properties: OUProps;
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OUProps`](#@renovosolutions/cdk-library-aws-organization.OUProps)

The OU object properties.

---

##### `accounts`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.accounts"></a>

```typescript
public readonly accounts: AccountProps[];
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.AccountProps`](#@renovosolutions/cdk-library-aws-organization.AccountProps)[]

Accounts that belong to this OU.

---

##### `id`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.id"></a>

```typescript
public readonly id: string;
```

- *Type:* `string`

The unique id of the OUObject.

This is used as the unique identifier when instantiating a construct object.
This is important for the CDK to be able to maintain a reference for the object when utilizing
the processOUObj function rather then using the name property of an object which could change.
If the id changes the CDK treats this as a new construct and will create a new construct resource and
destroy the old one.

Not strictly required but useful when using the processOUObj function. If the id is not provided
the name property will be used as the id in processOUObj.

You can create a unique id however you like. A bash example is provided.

---

### OUProps <a name="@renovosolutions/cdk-library-aws-organization.OUProps"></a>

The properties of an OU.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { OUProps } from '@renovosolutions/cdk-library-aws-organization'

const oUProps: OUProps = { ... }
```

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUProps.property.name"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the OU.

---

##### `allowRecreateOnUpdate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUProps.property.allowRecreateOnUpdate"></a>

```typescript
public readonly allowRecreateOnUpdate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not a missing OU should be recreated during an update.

If this is false and the OU does not exist an error will be thrown when you try to update it.

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUProps.property.importOnDuplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing OU if the new OU is a duplicate.

If this is false and the OU already exists an error will be thrown.

---

### OUResourceProps <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps"></a>

The properties of an OrganizationOU custom resource.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { OUResourceProps } from '@renovosolutions/cdk-library-aws-organization'

const oUResourceProps: OUResourceProps = { ... }
```

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.name"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the OU.

---

##### `allowRecreateOnUpdate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.allowRecreateOnUpdate"></a>

```typescript
public readonly allowRecreateOnUpdate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not a missing OU should be recreated during an update.

If this is false and the OU does not exist an error will be thrown when you try to update it.

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.importOnDuplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing OU if the new OU is a duplicate.

If this is false and the OU already exists an error will be thrown.

---

##### `parent`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.parent"></a>

```typescript
public readonly parent: string | OrganizationOU;
```

- *Type:* `string` | [`@renovosolutions/cdk-library-aws-organization.OrganizationOU`](#@renovosolutions/cdk-library-aws-organization.OrganizationOU)

The parent OU id.

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.provider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

The provider to use for the custom resource that will create the OU.

You can create a provider with the OrganizationOuProvider class

---



