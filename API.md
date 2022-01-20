# API Reference <a name="API Reference" id="api-reference"></a>

## Constructs <a name="Constructs" id="constructs"></a>

### IPAMAdministratorProvider <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProvider" id="renovosolutionscdklibraryawsorganizationipamadministratorprovider"></a>

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProvider.Initializer" id="renovosolutionscdklibraryawsorganizationipamadministratorproviderinitializer"></a>

```typescript
import { IPAMAdministratorProvider } from '@renovosolutions/cdk-library-aws-organization'

new IPAMAdministratorProvider(scope: Construct, id: string, props: IPAMAdministratorProviderProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#renovosolutionscdklibraryawsorganizationipamadministratorproviderparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#renovosolutionscdklibraryawsorganizationipamadministratorproviderparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#renovosolutionscdklibraryawsorganizationipamadministratorproviderparameterprops)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps`](#@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProvider.parameter.scope" id="renovosolutionscdklibraryawsorganizationipamadministratorproviderparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProvider.parameter.id" id="renovosolutionscdklibraryawsorganizationipamadministratorproviderparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProvider.parameter.props" id="renovosolutionscdklibraryawsorganizationipamadministratorproviderparameterprops"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps`](#@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`provider`](#renovosolutionscdklibraryawsorganizationipamadministratorproviderpropertyprovider)<span title="Required">*</span> | [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider) | *No description.* |

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProvider.property.provider" id="renovosolutionscdklibraryawsorganizationipamadministratorproviderpropertyprovider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

---


### IPAMdministrator <a name="@renovosolutions/cdk-library-aws-organization.IPAMdministrator" id="renovosolutionscdklibraryawsorganizationipamdministrator"></a>

The construct to create or update the delegated IPAM administrator for an organization.

This relies on the custom resource provider IPAMAdministratorProvider.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.IPAMdministrator.Initializer" id="renovosolutionscdklibraryawsorganizationipamdministratorinitializer"></a>

```typescript
import { IPAMdministrator } from '@renovosolutions/cdk-library-aws-organization'

new IPAMdministrator(scope: Construct, id: string, props: IPAMAdministratorProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#renovosolutionscdklibraryawsorganizationipamdministratorparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#renovosolutionscdklibraryawsorganizationipamdministratorparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#renovosolutionscdklibraryawsorganizationipamdministratorparameterprops)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps`](#@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMdministrator.parameter.scope" id="renovosolutionscdklibraryawsorganizationipamdministratorparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMdministrator.parameter.id" id="renovosolutionscdklibraryawsorganizationipamdministratorparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMdministrator.parameter.props" id="renovosolutionscdklibraryawsorganizationipamdministratorparameterprops"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps`](#@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`resource`](#renovosolutionscdklibraryawsorganizationipamdministratorpropertyresource)<span title="Required">*</span> | [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource) | *No description.* |

---

##### `resource`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMdministrator.property.resource" id="renovosolutionscdklibraryawsorganizationipamdministratorpropertyresource"></a>

```typescript
public readonly resource: CustomResource;
```

- *Type:* [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource)

---


### OrganizationAccount <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount" id="renovosolutionscdklibraryawsorganizationorganizationaccount"></a>

The construct to create or update an Organization account.

This relies on the custom resource provider OrganizationAccountProvider.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.Initializer" id="renovosolutionscdklibraryawsorganizationorganizationaccountinitializer"></a>

```typescript
import { OrganizationAccount } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationAccount(scope: Construct, id: string, props: AccountResourceProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#renovosolutionscdklibraryawsorganizationorganizationaccountparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#renovosolutionscdklibraryawsorganizationorganizationaccountparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#renovosolutionscdklibraryawsorganizationorganizationaccountparameterprops)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.AccountResourceProps`](#@renovosolutions/cdk-library-aws-organization.AccountResourceProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.parameter.scope" id="renovosolutionscdklibraryawsorganizationorganizationaccountparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.parameter.id" id="renovosolutionscdklibraryawsorganizationorganizationaccountparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.parameter.props" id="renovosolutionscdklibraryawsorganizationorganizationaccountparameterprops"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.AccountResourceProps`](#@renovosolutions/cdk-library-aws-organization.AccountResourceProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`resource`](#renovosolutionscdklibraryawsorganizationorganizationaccountpropertyresource)<span title="Required">*</span> | [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource) | *No description.* |

---

##### `resource`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccount.property.resource" id="renovosolutionscdklibraryawsorganizationorganizationaccountpropertyresource"></a>

```typescript
public readonly resource: CustomResource;
```

- *Type:* [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource)

---


### OrganizationAccountProvider <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider" id="renovosolutionscdklibraryawsorganizationorganizationaccountprovider"></a>

The provider for account custom resources.

This creates a lambda function that handles custom resource requests for creating/updating accounts.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.Initializer" id="renovosolutionscdklibraryawsorganizationorganizationaccountproviderinitializer"></a>

```typescript
import { OrganizationAccountProvider } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationAccountProvider(scope: Construct, id: string, props: OrganizationOUProviderProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#renovosolutionscdklibraryawsorganizationorganizationaccountproviderparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#renovosolutionscdklibraryawsorganizationorganizationaccountproviderparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#renovosolutionscdklibraryawsorganizationorganizationaccountproviderparameterprops)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps`](#@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.parameter.scope" id="renovosolutionscdklibraryawsorganizationorganizationaccountproviderparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.parameter.id" id="renovosolutionscdklibraryawsorganizationorganizationaccountproviderparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.parameter.props" id="renovosolutionscdklibraryawsorganizationorganizationaccountproviderparameterprops"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps`](#@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`provider`](#renovosolutionscdklibraryawsorganizationorganizationaccountproviderpropertyprovider)<span title="Required">*</span> | [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider) | *No description.* |

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProvider.property.provider" id="renovosolutionscdklibraryawsorganizationorganizationaccountproviderpropertyprovider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

---


### OrganizationOU <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU" id="renovosolutionscdklibraryawsorganizationorganizationou"></a>

The construct to create or update an Organization OU.

This relies on the custom resource provider OrganizationOUProvider.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.Initializer" id="renovosolutionscdklibraryawsorganizationorganizationouinitializer"></a>

```typescript
import { OrganizationOU } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationOU(scope: Construct, id: string, props: OUResourceProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#renovosolutionscdklibraryawsorganizationorganizationouparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#renovosolutionscdklibraryawsorganizationorganizationouparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#renovosolutionscdklibraryawsorganizationorganizationouparameterprops)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.OUResourceProps`](#@renovosolutions/cdk-library-aws-organization.OUResourceProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.scope" id="renovosolutionscdklibraryawsorganizationorganizationouparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.id" id="renovosolutionscdklibraryawsorganizationorganizationouparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.parameter.props" id="renovosolutionscdklibraryawsorganizationorganizationouparameterprops"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OUResourceProps`](#@renovosolutions/cdk-library-aws-organization.OUResourceProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`resource`](#renovosolutionscdklibraryawsorganizationorganizationoupropertyresource)<span title="Required">*</span> | [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource) | *No description.* |

---

##### `resource`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU.property.resource" id="renovosolutionscdklibraryawsorganizationorganizationoupropertyresource"></a>

```typescript
public readonly resource: CustomResource;
```

- *Type:* [`aws-cdk-lib.CustomResource`](#aws-cdk-lib.CustomResource)

---


### OrganizationOUProvider <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider" id="renovosolutionscdklibraryawsorganizationorganizationouprovider"></a>

The provider for OU custom resources.

This creates a lambda function that handles custom resource requests for creating/updating/deleting OUs.

#### Initializers <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.Initializer" id="renovosolutionscdklibraryawsorganizationorganizationouproviderinitializer"></a>

```typescript
import { OrganizationOUProvider } from '@renovosolutions/cdk-library-aws-organization'

new OrganizationOUProvider(scope: Construct, id: string, props: OrganizationOUProviderProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`scope`](#renovosolutionscdklibraryawsorganizationorganizationouproviderparameterscope)<span title="Required">*</span> | [`constructs.Construct`](#constructs.Construct) | *No description.* |
| [`id`](#renovosolutionscdklibraryawsorganizationorganizationouproviderparameterid)<span title="Required">*</span> | `string` | *No description.* |
| [`props`](#renovosolutionscdklibraryawsorganizationorganizationouproviderparameterprops)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps`](#@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps) | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.parameter.scope" id="renovosolutionscdklibraryawsorganizationorganizationouproviderparameterscope"></a>

- *Type:* [`constructs.Construct`](#constructs.Construct)

---

##### `id`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.parameter.id" id="renovosolutionscdklibraryawsorganizationorganizationouproviderparameterid"></a>

- *Type:* `string`

---

##### `props`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.parameter.props" id="renovosolutionscdklibraryawsorganizationorganizationouproviderparameterprops"></a>

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps`](#@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps)

---



#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`provider`](#renovosolutionscdklibraryawsorganizationorganizationouproviderpropertyprovider)<span title="Required">*</span> | [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider) | *No description.* |

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider.property.provider" id="renovosolutionscdklibraryawsorganizationorganizationouproviderpropertyprovider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

---


## Structs <a name="Structs" id="structs"></a>

### AccountProps <a name="@renovosolutions/cdk-library-aws-organization.AccountProps" id="renovosolutionscdklibraryawsorganizationaccountprops"></a>

The properties of an Account.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { AccountProps } from '@renovosolutions/cdk-library-aws-organization'

const accountProps: AccountProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`email`](#renovosolutionscdklibraryawsorganizationaccountpropspropertyemail)<span title="Required">*</span> | `string` | The email address of the account. |
| [`name`](#renovosolutionscdklibraryawsorganizationaccountpropspropertyname)<span title="Required">*</span> | `string` | The name of the account. |
| [`allowMove`](#renovosolutionscdklibraryawsorganizationaccountpropspropertyallowmove) | `boolean` | Whether or not to allow this account to be moved between OUs. |
| [`disableDelete`](#renovosolutionscdklibraryawsorganizationaccountpropspropertydisabledelete) | `boolean` | Whether or not attempting to delete an account should raise an error. |
| [`importOnDuplicate`](#renovosolutionscdklibraryawsorganizationaccountpropspropertyimportonduplicate) | `boolean` | Whether or not to import an existing account if the new account is a duplicate. |

---

##### `email`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.email" id="renovosolutionscdklibraryawsorganizationaccountpropspropertyemail"></a>

```typescript
public readonly email: string;
```

- *Type:* `string`

The email address of the account.

Most be unique.

---

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.name" id="renovosolutionscdklibraryawsorganizationaccountpropspropertyname"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the account.

---

##### `allowMove`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.allowMove" id="renovosolutionscdklibraryawsorganizationaccountpropspropertyallowmove"></a>

```typescript
public readonly allowMove: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to allow this account to be moved between OUs.

If importing is enabled this will also allow imported accounts to be moved.

---

##### `disableDelete`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.disableDelete" id="renovosolutionscdklibraryawsorganizationaccountpropspropertydisabledelete"></a>

```typescript
public readonly disableDelete: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not attempting to delete an account should raise an error.

Accounts cannot be deleted programmatically, but they can be removed as a managed resource. This property will allow you to control whether or not an error is thrown when the stack wants to delete an account (orphan it) or if it should continue silently.

> https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountProps.property.importOnDuplicate" id="renovosolutionscdklibraryawsorganizationaccountpropspropertyimportonduplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing account if the new account is a duplicate.

If this is false and the account already exists an error will be thrown.

---

### AccountResourceProps <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps" id="renovosolutionscdklibraryawsorganizationaccountresourceprops"></a>

The properties of an OrganizationAccount custom resource.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { AccountResourceProps } from '@renovosolutions/cdk-library-aws-organization'

const accountResourceProps: AccountResourceProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`email`](#renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyemail)<span title="Required">*</span> | `string` | The email address of the account. |
| [`name`](#renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyname)<span title="Required">*</span> | `string` | The name of the account. |
| [`allowMove`](#renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyallowmove) | `boolean` | Whether or not to allow this account to be moved between OUs. |
| [`disableDelete`](#renovosolutionscdklibraryawsorganizationaccountresourcepropspropertydisabledelete) | `boolean` | Whether or not attempting to delete an account should raise an error. |
| [`importOnDuplicate`](#renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyimportonduplicate) | `boolean` | Whether or not to import an existing account if the new account is a duplicate. |
| [`parent`](#renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyparent)<span title="Required">*</span> | `string` \| [`@renovosolutions/cdk-library-aws-organization.OrganizationOU`](#@renovosolutions/cdk-library-aws-organization.OrganizationOU) | The parent OU id. |
| [`provider`](#renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyprovider)<span title="Required">*</span> | [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider) | The provider to use for the custom resource that will create the OU. |

---

##### `email`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.email" id="renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyemail"></a>

```typescript
public readonly email: string;
```

- *Type:* `string`

The email address of the account.

Most be unique.

---

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.name" id="renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyname"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the account.

---

##### `allowMove`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.allowMove" id="renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyallowmove"></a>

```typescript
public readonly allowMove: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to allow this account to be moved between OUs.

If importing is enabled this will also allow imported accounts to be moved.

---

##### `disableDelete`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.disableDelete" id="renovosolutionscdklibraryawsorganizationaccountresourcepropspropertydisabledelete"></a>

```typescript
public readonly disableDelete: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not attempting to delete an account should raise an error.

Accounts cannot be deleted programmatically, but they can be removed as a managed resource. This property will allow you to control whether or not an error is thrown when the stack wants to delete an account (orphan it) or if it should continue silently.

> https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.importOnDuplicate" id="renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyimportonduplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing account if the new account is a duplicate.

If this is false and the account already exists an error will be thrown.

---

##### `parent`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.parent" id="renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyparent"></a>

```typescript
public readonly parent: string | OrganizationOU;
```

- *Type:* `string` | [`@renovosolutions/cdk-library-aws-organization.OrganizationOU`](#@renovosolutions/cdk-library-aws-organization.OrganizationOU)

The parent OU id.

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.AccountResourceProps.property.provider" id="renovosolutionscdklibraryawsorganizationaccountresourcepropspropertyprovider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

The provider to use for the custom resource that will create the OU.

You can create a provider with the OrganizationOuProvider class

---

### OrganizationAccountProviderProps <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProviderProps" id="renovosolutionscdklibraryawsorganizationorganizationaccountproviderprops"></a>

The properties for the account custom resource provider.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { OrganizationAccountProviderProps } from '@renovosolutions/cdk-library-aws-organization'

const organizationAccountProviderProps: OrganizationAccountProviderProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`role`](#renovosolutionscdklibraryawsorganizationorganizationaccountproviderpropspropertyrole) | [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole) | The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically. |

---

##### `role`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationAccountProviderProps.property.role" id="renovosolutionscdklibraryawsorganizationorganizationaccountproviderpropspropertyrole"></a>

```typescript
public readonly role: IRole;
```

- *Type:* [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole)

The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically.

---

### OrganizationOUProviderProps <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps" id="renovosolutionscdklibraryawsorganizationorganizationouproviderprops"></a>

The properties for the OU custom resource provider.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { OrganizationOUProviderProps } from '@renovosolutions/cdk-library-aws-organization'

const organizationOUProviderProps: OrganizationOUProviderProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`role`](#renovosolutionscdklibraryawsorganizationorganizationouproviderpropspropertyrole) | [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole) | The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically. |

---

##### `role`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps.property.role" id="renovosolutionscdklibraryawsorganizationorganizationouproviderpropspropertyrole"></a>

```typescript
public readonly role: IRole;
```

- *Type:* [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole)

The role the custom resource should use for taking actions on OUs if one is not provided one will be created automatically.

---

### OUObject <a name="@renovosolutions/cdk-library-aws-organization.OUObject" id="renovosolutionscdklibraryawsorganizationouobject"></a>

The structure of an OrgObject.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { OUObject } from '@renovosolutions/cdk-library-aws-organization'

const oUObject: OUObject = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`children`](#renovosolutionscdklibraryawsorganizationouobjectpropertychildren)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.OUObject`](#@renovosolutions/cdk-library-aws-organization.OUObject)[] | OUs that are children of this OU. |
| [`properties`](#renovosolutionscdklibraryawsorganizationouobjectpropertyproperties)<span title="Required">*</span> | [`@renovosolutions/cdk-library-aws-organization.OUProps`](#@renovosolutions/cdk-library-aws-organization.OUProps) | The OU object properties. |
| [`accounts`](#renovosolutionscdklibraryawsorganizationouobjectpropertyaccounts) | [`@renovosolutions/cdk-library-aws-organization.AccountProps`](#@renovosolutions/cdk-library-aws-organization.AccountProps)[] | Accounts that belong to this OU. |
| [`id`](#renovosolutionscdklibraryawsorganizationouobjectpropertyid) | `string` | The unique id of the OUObject. |

---

##### `children`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.children" id="renovosolutionscdklibraryawsorganizationouobjectpropertychildren"></a>

```typescript
public readonly children: OUObject[];
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OUObject`](#@renovosolutions/cdk-library-aws-organization.OUObject)[]

OUs that are children of this OU.

---

##### `properties`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.properties" id="renovosolutionscdklibraryawsorganizationouobjectpropertyproperties"></a>

```typescript
public readonly properties: OUProps;
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.OUProps`](#@renovosolutions/cdk-library-aws-organization.OUProps)

The OU object properties.

---

##### `accounts`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.accounts" id="renovosolutionscdklibraryawsorganizationouobjectpropertyaccounts"></a>

```typescript
public readonly accounts: AccountProps[];
```

- *Type:* [`@renovosolutions/cdk-library-aws-organization.AccountProps`](#@renovosolutions/cdk-library-aws-organization.AccountProps)[]

Accounts that belong to this OU.

---

##### `id`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUObject.property.id" id="renovosolutionscdklibraryawsorganizationouobjectpropertyid"></a>

```typescript
public readonly id: string;
```

- *Type:* `string`

The unique id of the OUObject.

This is used as the unique identifier when instantiating a construct object. This is important for the CDK to be able to maintain a reference for the object when utilizing the processOUObj function rather then using the name property of an object which could change. If the id changes the CDK treats this as a new construct and will create a new construct resource and destroy the old one.  Not strictly required but useful when using the processOUObj function. If the id is not provided the name property will be used as the id in processOUObj.  You can create a unique id however you like. A bash example is provided.

---

### OUProps <a name="@renovosolutions/cdk-library-aws-organization.OUProps" id="renovosolutionscdklibraryawsorganizationouprops"></a>

The properties of an OU.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { OUProps } from '@renovosolutions/cdk-library-aws-organization'

const oUProps: OUProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`name`](#renovosolutionscdklibraryawsorganizationoupropspropertyname)<span title="Required">*</span> | `string` | The name of the OU. |
| [`allowRecreateOnUpdate`](#renovosolutionscdklibraryawsorganizationoupropspropertyallowrecreateonupdate) | `boolean` | Whether or not a missing OU should be recreated during an update. |
| [`importOnDuplicate`](#renovosolutionscdklibraryawsorganizationoupropspropertyimportonduplicate) | `boolean` | Whether or not to import an existing OU if the new OU is a duplicate. |

---

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUProps.property.name" id="renovosolutionscdklibraryawsorganizationoupropspropertyname"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the OU.

---

##### `allowRecreateOnUpdate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUProps.property.allowRecreateOnUpdate" id="renovosolutionscdklibraryawsorganizationoupropspropertyallowrecreateonupdate"></a>

```typescript
public readonly allowRecreateOnUpdate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not a missing OU should be recreated during an update.

If this is false and the OU does not exist an error will be thrown when you try to update it.

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUProps.property.importOnDuplicate" id="renovosolutionscdklibraryawsorganizationoupropspropertyimportonduplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing OU if the new OU is a duplicate.

If this is false and the OU already exists an error will be thrown.

---

### OUResourceProps <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps" id="renovosolutionscdklibraryawsorganizationouresourceprops"></a>

The properties of an OrganizationOU custom resource.

#### Initializer <a name="[object Object].Initializer" id="object-objectinitializer"></a>

```typescript
import { OUResourceProps } from '@renovosolutions/cdk-library-aws-organization'

const oUResourceProps: OUResourceProps = { ... }
```

#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`name`](#renovosolutionscdklibraryawsorganizationouresourcepropspropertyname)<span title="Required">*</span> | `string` | The name of the OU. |
| [`allowRecreateOnUpdate`](#renovosolutionscdklibraryawsorganizationouresourcepropspropertyallowrecreateonupdate) | `boolean` | Whether or not a missing OU should be recreated during an update. |
| [`importOnDuplicate`](#renovosolutionscdklibraryawsorganizationouresourcepropspropertyimportonduplicate) | `boolean` | Whether or not to import an existing OU if the new OU is a duplicate. |
| [`parent`](#renovosolutionscdklibraryawsorganizationouresourcepropspropertyparent)<span title="Required">*</span> | `string` \| [`@renovosolutions/cdk-library-aws-organization.OrganizationOU`](#@renovosolutions/cdk-library-aws-organization.OrganizationOU) | The parent OU id. |
| [`provider`](#renovosolutionscdklibraryawsorganizationouresourcepropspropertyprovider)<span title="Required">*</span> | [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider) | The provider to use for the custom resource that will create the OU. |

---

##### `name`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.name" id="renovosolutionscdklibraryawsorganizationouresourcepropspropertyname"></a>

```typescript
public readonly name: string;
```

- *Type:* `string`

The name of the OU.

---

##### `allowRecreateOnUpdate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.allowRecreateOnUpdate" id="renovosolutionscdklibraryawsorganizationouresourcepropspropertyallowrecreateonupdate"></a>

```typescript
public readonly allowRecreateOnUpdate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not a missing OU should be recreated during an update.

If this is false and the OU does not exist an error will be thrown when you try to update it.

---

##### `importOnDuplicate`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.importOnDuplicate" id="renovosolutionscdklibraryawsorganizationouresourcepropspropertyimportonduplicate"></a>

```typescript
public readonly importOnDuplicate: boolean;
```

- *Type:* `boolean`
- *Default:* false

Whether or not to import an existing OU if the new OU is a duplicate.

If this is false and the OU already exists an error will be thrown.

---

##### `parent`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.parent" id="renovosolutionscdklibraryawsorganizationouresourcepropspropertyparent"></a>

```typescript
public readonly parent: string | OrganizationOU;
```

- *Type:* `string` | [`@renovosolutions/cdk-library-aws-organization.OrganizationOU`](#@renovosolutions/cdk-library-aws-organization.OrganizationOU)

The parent OU id.

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OUResourceProps.property.provider" id="renovosolutionscdklibraryawsorganizationouresourcepropspropertyprovider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

The provider to use for the custom resource that will create the OU.

You can create a provider with the OrganizationOuProvider class

---


## Protocols <a name="Protocols" id="protocols"></a>

### IPAMAdministratorProps <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps" id="renovosolutionscdklibraryawsorganizationipamadministratorprops"></a>

- *Implemented By:* [`@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps`](#@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps)

The properties of an OrganizationAccount custom resource.


#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`delegatedAdminAccountId`](#renovosolutionscdklibraryawsorganizationipamadministratorpropspropertydelegatedadminaccountid)<span title="Required">*</span> | `string` | The account id of the IPAM administrator. |
| [`provider`](#renovosolutionscdklibraryawsorganizationipamadministratorpropspropertyprovider)<span title="Required">*</span> | [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider) | The provider to use for the custom resource that will handle IPAM admin delegation. |

---

##### `delegatedAdminAccountId`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps.property.delegatedAdminAccountId" id="renovosolutionscdklibraryawsorganizationipamadministratorpropspropertydelegatedadminaccountid"></a>

```typescript
public readonly delegatedAdminAccountId: string;
```

- *Type:* `string`

The account id of the IPAM administrator.

---

##### `provider`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProps.property.provider" id="renovosolutionscdklibraryawsorganizationipamadministratorpropspropertyprovider"></a>

```typescript
public readonly provider: Provider;
```

- *Type:* [`aws-cdk-lib.custom_resources.Provider`](#aws-cdk-lib.custom_resources.Provider)

The provider to use for the custom resource that will handle IPAM admin delegation.

You can create a provider with the IPAMAdministratorProvider class

---

### IPAMAdministratorProviderProps <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps" id="renovosolutionscdklibraryawsorganizationipamadministratorproviderprops"></a>

- *Implemented By:* [`@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps`](#@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps)

The properties of an IPAM administrator custom resource provider.


#### Properties <a name="Properties" id="properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| [`role`](#renovosolutionscdklibraryawsorganizationipamadministratorproviderpropspropertyrole) | [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole) | The role the custom resource should use for working with the IPAM administrator delegation if one is not provided one will be created automatically. |

---

##### `role`<sup>Optional</sup> <a name="@renovosolutions/cdk-library-aws-organization.IPAMAdministratorProviderProps.property.role" id="renovosolutionscdklibraryawsorganizationipamadministratorproviderpropspropertyrole"></a>

```typescript
public readonly role: IRole;
```

- *Type:* [`aws-cdk-lib.aws_iam.IRole`](#aws-cdk-lib.aws_iam.IRole)

The role the custom resource should use for working with the IPAM administrator delegation if one is not provided one will be created automatically.

---

