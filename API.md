# API Reference <a name="API Reference"></a>

## Constructs <a name="Constructs"></a>

### OrganizationOU <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU"></a>

The construct to create or update an Organization OU.

This relies on the custom resource provider OrganizationOUProvider.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.Initializer"></a>

```typescript
import { OrganizationOU } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationOU(scope: Construct, id: string, props: OrganizationOUProps)
```

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.scope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.id"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.props"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OrganizationOUProps`](#@renovosolutions/cdk-library-aws-organization.OrganizationOUProps)

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

### OrganizationOUProps <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps"></a>

The properties of an OrganizationOU custom resource.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { OrganizationOUProps } from '@renovosolutions/cdk-library-aws-organization'

const organizationOUProps: OrganizationOUProps = { ... }
```

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps.property.name"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the OU.

---

##### `parent`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps.property.parent"></a>

```typescript
public readonly parent: string | OrganizationOU;
```

- *Type:* `string` | [`@renovosolutions/cdk-library-aws-organization.OrganizationOU`](#@renovosolutions/cdk-library-aws-organization.OrganizationOU)

The parent OU id.

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps.property.provider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

The provider to use for the custom resource that will create the OU.

You can create a provider with the OrganizationOuProvider class

---

##### `allowMergeOnMove`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps.property.allowMergeOnMove"></a>

```typescript
public readonly allowMergeOnMove: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to merge an OU with a duplicate when an OU is moved between parent OUs.

If this is false and the OU already exists an error will be thrown.
If this is true and the OU already exists the accounts in the OU will be moved to the existing OU
and the duplicate, now empty, OU will be deleted.

---

##### `allowRecreateOnUpdate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps.property.allowRecreateOnUpdate"></a>

```typescript
public readonly allowRecreateOnUpdate: boolean;
```

- *Type:* `boolean`

Whether or not a missing OU should be recreated during an update.

If this is false and the OU does not exist an error will be thrown when you try to update it.

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps.property.importOnDuplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing OU if the new OU is a duplicate.

If this is false and the OU already exists an error will be thrown.

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

### OrgObject <a name="@renovosolutions/cdk-library-aws-organization.OrgObject"></a>

The structure of an OrgObject.

#### Initializer <a name="[object Object].Initializer"></a>

```typescript
import { OrgObject } from '@renovosolutions/cdk-library-aws-organization'

const orgObject: OrgObject = { ... }
```

##### `children`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrgObject.property.children"></a>

```typescript
public readonly children: OrgObject[];
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OrgObject`](#@renovosolutions/cdk-library-aws-organization.OrgObject)[]

Other org objects that are children of this org object.

---

##### `properties`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrgObject.property.properties"></a>

```typescript
public readonly properties: OUProps | AccountProps;
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OUProps`](#@renovosolutions/cdk-library-aws-organization.OUProps) | [`@renovosolutions/cdk-library-aws-organization.AccountProps`](#@renovosolutions/cdk-library-aws-organization.AccountProps)

The org object properties.

---

##### `type`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrgObject.property.type"></a>

```typescript
public readonly type: OrgObjectTypes;
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OrgObjectTypes`](#@renovosolutions/cdk-library-aws-organization.OrgObjectTypes)

The type of the org object.

---

##### `id`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrgObject.property.id"></a>

```typescript
public readonly id: string;
```

- *Type:* `string`

The unique id of the OrgObject.

This is used as the unique identifier when instantiating a construct object.
This is important for the CDK to be able to maintain a reference for the object when utilizing
the processOrgObj function rather then using the name property of an object which could change.
If the id changes the CDK treats this as a new construct and will create a new construct resource and
destroy the old one.

Not strictly required but useful when using the processOrgObj function. If the id is not provided
the name property will be used as the id in processOrgObj.

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



## Enums <a name="Enums"></a>

### OrgObjectTypes <a name="OrgObjectTypes"></a>

The supported OrgObject types.

#### `OU` <a name="@renovosolutions/cdk-library-aws-organization.OrgObjectTypes.OU"></a>

---


#### `ACCOUNT` <a name="@renovosolutions/cdk-library-aws-organization.OrgObjectTypes.ACCOUNT"></a>

---

