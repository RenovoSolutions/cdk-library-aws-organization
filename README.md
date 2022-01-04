# cdk-library-aws-organization

This CDK library is a WIP and not ready for production use.

## Key challenges with Organizations
- Accounts aren't like AWS resources and the [removal process isn't a simple delete](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html). Therefore the constructs contained in this library do **not** have the goal to delete accounts.
- CloudFormation doesn't support Organizations directly so the constructs in this library use CloudFormation custom resources that utilize Python and [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html)

## Testing the custom provider code with SAM CLI

**Pre-reqs**
- You will either want a previously created test account or allow the tests to create a new account

**Testing**
- Create a test project that utilizes this library
- Create a test stack
- Synthesize the test stack with `cdk synth --no-staging > template.yml`
- Get the handler function names from the template
- Run `sam local start-lambda -t template.yml`
- Run the `handler_tests` python files with `pytest` like follows:
```
TEST_ACCOUNT_NAME='<name>' TEST_ACCOUNT_EMAIL='<email>' TEST_ACCOUNT_ORIGINAL_OU='<original ou id>' ACCOUNT_LAMBDA_FUNCTION_NAME='<name you noted earlier>' OU_LAMBDA_FUNCTION_NAME='<name you noted earlier>' pytest ./handler_tests/<handler>/test.py -rA --capture=sys
```
- Using the name, email, and original OU env variables here allows the test suite to re-use a single test account. Given deleting accounts is not simple you likely dont want to randomly create a new account every time you run tests.
- The `test.py` also looks up the root org id to run tests so you'll need to have AWS creds set up to accomodate that behavior.
- You can run the provided tests against the real lambda function by getting the deployed function name from AWS and setting the `RUN_LOCALLY` env variable
```
TEST_ACCOUNT_NAME='<name>' TEST_ACCOUNT_EMAIL='<email>' TEST_ACCOUNT_ORIGINAL_OU='<original ou id>' RUN_LOCALLY='false' ACCOUNT_LAMBDA_FUNCTION_NAME='<name you noted earlier>' OU_LAMBDA_FUNCTION_NAME='<name from AWS>' pytest ./handler_tests/<handler>/test.py -rA --capture=sys
```

## Why can't I move an OU?
Moving OUs isn't supported by Organizations and would cause significant issues with keeping track of OUs in the CDK. Imagine a scenario like below:
- You have an ou, `OUAdmin`, and it has 2 children, `OUChild1 and Account1`, that are also managed by the CDK stack.
- You change the parent of `OUAdmin` to `OUFoo`. The CDK would need to take the following actions:
  - Create a new `OU` under `OUFoo` with the name `OUAdmin`
  - Move all of the original `OUAdmin` OU's children to the new `OUAdmin`
  - Delete the old `OUAdmin`
  - Update all physical resource IDs
    - It would succeed at moving accounts because physical IDs should not change. Accounting moving between OUs is supported by Organizations
    - It would fail at moving any child OUs because they would also be recreated. Resulting in a change to physical resource ID. Because the custom resource can only managed the resource it's currently acting on, `OUAdmin`, any children OUs would be "lost" in this process and ugly to try and manage.

The best way to move OUs would be to add additional OUs to your org then move any accounts as needed then proceed to delete the OUs, like so:
- Add new OU resources
- Deploy the stack
- Change account parents
- Deploy the stack
- Remove old OU resources
- Deploy the stack
