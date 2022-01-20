import { Stack, App } from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import {
  OrganizationOUProvider,
  OUObject,
  processOUObj,
  OrganizationAccountProvider,
  IPAMAdministratorProvider,
  IPAMdministrator,
} from '../src/index';

test('Snapshot', () => {
  const app = new App();
  const stack = new Stack(app, 'TestStack');

  const ouProvider = new OrganizationOUProvider(stack, 'OrganizationOUProvider', {}).provider;
  const accountProvider = new OrganizationAccountProvider(stack, 'OrganizationAccountProvider', {}).provider;
  const ipamProvider = new IPAMAdministratorProvider(stack, 'IPAMAdministratorProvider', {}).provider;

  const orgStructure: OUObject[] = [
    {
      id: 'ou-301416f8',
      properties: {
        name: 'TestOU',
      },
      children: [
        {
          id: 'ou-df425b37',
          properties: {
            name: 'TestOUChild',
          },
          children: [
          ],
          accounts: [
            {
              name: 'TestAccount',
              email: 'test@example.com',
            },
          ],
        },
      ],
    },
  ];

  orgStructure.forEach(obj => {
    processOUObj.call(stack, ouProvider, accountProvider, obj, 'r-a1b2');
  });

  new IPAMdministrator(stack, 'IPAMAdministrator', {
    provider: ipamProvider,
    delegatedAdminAccountId: '123456789012',
  });

  expect(Template.fromStack(stack)).toMatchSnapshot();
});
