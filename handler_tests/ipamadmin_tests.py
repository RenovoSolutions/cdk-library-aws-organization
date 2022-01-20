import boto3
import botocore
import json
import os

running_locally = True

if os.getenv("RUN_LOCALLY") == "false":
  running_locally = False

if running_locally:
  lambda_client = boto3.client('lambda',
    region_name="us-east-1",
    endpoint_url="http://127.0.0.1:3001",
    use_ssl=False,
    verify=False,
    config=botocore.client.Config(
      signature_version=botocore.UNSIGNED,
      read_timeout=300,
      retries={'max_attempts': 0},
    )
  )
else:
  lambda_client = boto3.client('lambda')
  
test_account_id = '123456789012'
if 'TEST_IPAM_ACCOUNT_ID' in os.environ: # use actual IPAM admin account here
  test_account_id = os.environ['TEST_IPAM_ACCOUNT_ID']
second_account_id = '123456789012'
if 'SECOND_ACCOUNT_ID' in os.environ: # use a test account here
  second_account_id = os.environ['SECOND_ACCOUNT_ID']
if 'LAMBDA_FUNCTION_NAME' in os.environ:
  print('LAMBDA_FUNCTION_NAME: ' + os.environ['LAMBDA_FUNCTION_NAME'])
else:
  raise Exception('LAMBDA_FUNCTION_NAME not set')

def update_ipamadmin_payload(payload, test_account_id, second_account_id=None):
  payload_str = json.load(payload)
  payload_str['ResourceProperties']['DelegatedAdminAccountId'] = test_account_id
  if 'PhysicalResourceId' in payload_str:
    payload_str['PhysicalResourceId'] = test_account_id
  if 'OldResourceProperties' in payload_str:
    payload_str['OldResourceProperties']['DelegatedAdminAccountId'] = second_account_id
  payload_bytes_arr = bytes(json.dumps(payload_str), encoding="utf8")
  print('PAYLOAD: ' + json.dumps(payload_str))
  return payload_bytes_arr

def test_designating_an_ipam_admin_should_succeed():
  global test_account_id
  f = open('events/ipamadmin/create.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_ipamadmin_payload(f, test_account_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['PhysicalResourceId'] == test_account_id
  assert response_json['Data']['Message'] == 'IPAM admin account successfully enabled'
  
def test_designating_an_account_not_in_the_org_should_fail():
  f = open('events/ipamadmin/create.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_ipamadmin_payload(f, '123456789012')
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'The specified account does not belong to your organization.'
  
def test_designating_a_second_ipam_admin_should_fail():
  global second_account_id
  f = open('events/ipamadmin/create.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_ipamadmin_payload(f, second_account_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'An IPAM delegated admin already exists and you may only specify one.'
  
def test_changing_an_admin_should_succeed():
  global test_account_id
  global second_account_id
  f = open('events/ipamadmin/update.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_ipamadmin_payload(f, second_account_id, test_account_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['PhysicalResourceId'] == second_account_id
  assert response_json['Data']['Message'] == 'IPAM admin account successfully enabled'
  
def test_changing_admin_back_should_succeed():
  global test_account_id
  global second_account_id
  f = open('events/ipamadmin/update.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_ipamadmin_payload(f, test_account_id, second_account_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['PhysicalResourceId'] == test_account_id
  assert response_json['Data']['Message'] == 'IPAM admin account successfully enabled'

def test_deleting_an_admin_should_succeed():
  global test_account_id
  f = open('events/ipamadmin/delete.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_ipamadmin_payload(f, test_account_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['PhysicalResourceId'] == test_account_id
  assert response_json['Data']['Message'] == 'IPAM admin account successfully disabled'
  
def test_deleting_an_admin_thats_already_deleted_should_succeed():
  global test_account_id
  f = open('events/ipamadmin/delete.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_ipamadmin_payload(f, test_account_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['PhysicalResourceId'] == test_account_id
  assert response_json['Data']['Message'] == 'No IPAM delegation exists for this organization and only one can exists. Assuming this delegation was already removed.'
  

