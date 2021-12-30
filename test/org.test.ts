import { Stack, App } from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import {
  OrganizationOUProvider,
  OrgObjectTypes,
  OrgObject,
  processOrgObj,
} from '../src/index';

test('Snapshot', () => {
  const app = new App();
  const stack = new Stack(app, 'TestStack');

  const provider = new OrganizationOUProvider(stack, 'OrganizationOUProvider', {}).provider;

  const orgStructure: OrgObject[] = [
    {
      id: 'ou-301416f8',
      properties: {
        name: 'TestOU',
      },
      type: OrgObjectTypes.OU,
      children: [
        {
          id: 'ou-df425b37',
          properties: {
            name: 'TestOUChild',
          },
          type: OrgObjectTypes.OU,
          children: [],
        },
      ],
    },
  ];

  orgStructure.forEach(obj => {
    processOrgObj.call(stack, provider, obj, 'r-a1b2');
  });

  expect(Template.fromStack(stack)).toMatchSnapshot();
});
