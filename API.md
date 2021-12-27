# API Reference <a name="API Reference"></a>

## Constructs <a name="Constructs"></a>

### OrganizationOU <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOU"></a>

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





### OrganizationOUProvider <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProvider"></a>

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

### OrganizationOUProps <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps"></a>

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

##### `parentId`<sup>Required</sup> <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProps.property.parentId"></a>

```typescript
public readonly parentId: string;
```

- *Type:* `string`

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

### OrganizationOUProviderProps <a name="@renovosolutions/cdk-library-aws-organization.OrganizationOUProviderProps"></a>

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



