# cdk-library-aws-organization

This CDK library is a WIP and not ready for production use.

## Key challenges with Organizations
- Accounts aren't like AWS resources and the [removal process isn't a simple delete](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html). Therefore the constructs contained in this library do **not** have the goal to delete accounts.
- CloudFormation doesn't support Organizations directly so the constructs in this library use CloudFormation custom resources that utilize Python and [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html)

## Testing the custom provider code with SAM CLI

- Create a test project that utilizes this library
- Create a test stack
- Synthesize the test stack with `cdk synth --no-staging > template.yml`
- Get the function name from the template
- Run `sam local start-lambda -t template.yml`
- Run the `handler_tests` python files with `pytest` like follows:
```
LAMBDA_FUNCTION_NAME='<name you noted earlier>' pytest ./handler_tests/<handler>/test.py -rA --capture=sys
```
- The `test.py` also looks up the root org id to run tests so you'll need to have AWS creds set up to accomodate that behavior.
- You can run the provided tests against the real lambda function by getting the deployed function name from AWS and setting the `RUN_LOCALLY` env variable
```
RUN_LOCALLY='false' LAMBDA_FUNCTION_NAME='<name from AWS>' pytest ./handler_tests/<handler>/test.py -rA --capture=sys
```
