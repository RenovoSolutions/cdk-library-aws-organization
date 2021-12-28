# cdk-library-aws-organization

This CDK library is a WIP and not ready for production use.

## Testing the custom provider code with SAM CLI

- Create a test project that utilizes this library
- Create a test stack
- Synthesize the test stack with `cdk synth --no-staging > template.yml`
- Run `sam local invoke <function from stack> -e <event json file>`
- There is some example events provided in the `events` folder, but you will need a real test org to run events against
