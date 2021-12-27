import { Stack, App } from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { OrganizationOU, OrganizationOUProvider } from '../src/index';

test('Snapshot', () => {
  const app = new App();
  const stack = new Stack(app, 'TestStack');

  new OrganizationOU(stack, 'ou', {
    name: 'test',
    parentId: 'r-1234',
    provider: new OrganizationOUProvider(stack, 'provider', {}).provider,
  });

  expect(Template.fromStack(stack)).toMatchSnapshot();
});
