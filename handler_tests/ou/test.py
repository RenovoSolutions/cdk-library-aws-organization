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
      read_timeout=10,
      retries={'max_attempts': 0},
    )
  )
else:
  lambda_client = boto3.client('lambda')

ou_id = ''
child_id = ''

def get_root():
  organizations = boto3.client('organizations')
  response = organizations.list_roots()
  return response['Roots'][0]['Id']

parent_id = get_root()

# Updates the payload loaded from the events folder with the ou id created during the tests and the root from the current account
def update_payload(payload, ou, parent_id, update_all_parents=True):
  payload_str = json.load(payload)
  if 'PhysicalResourceId' in payload_str:
    payload_str['PhysicalResourceId'] = ou
  payload_str['ResourceProperties']['Parent'] = parent_id
  if 'OldResourceProperties' in payload_str and update_all_parents:
    payload_str['OldResourceProperties']['Parent'] = parent_id
  payload_bytes_arr = bytes(json.dumps(payload_str), encoding="utf8")
  return payload_bytes_arr

def test_create_with_import_should_create_or_import_ou():
  global ou_id
  f = open('events/ou/create-with-import.json', 'r')
  global parent_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, '', parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  ou_id = response_json['PhysicalResourceId']
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  
  assert response_json['Data']['Message'] == 'Created new OU: TestOULib' or 'Imported existing OU with same properties: ou-' in response_json['Data']['Message']

def test_create_without_import_should_fail_with_exception():
  f = open('events/ou/create-no-import.json', 'r')
  global parent_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, '', parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'OU already exists and import is disabled: TestOULib'
  
def test_delete_should_delete_ou():
  f = open('events/ou/delete.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Deleted OU: TestOULib'
  
def test_delete_again_should_notify_already_deleted():
  f = open('events/ou/delete.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'OU has already been deleted: TestOULib'
  
def test_update_when_deleted_should_fail_with_exception():
  f = open('events/ou/update.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'The OU you are trying to update, TestOULib, does not exist and creation of missing OUs on update is disabled.'
  
def test_update_with_recreate_should_create_OU_when_old_ou_does_not_exist():
  f = open('events/ou/update-with-recreate.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  ou_id = response_json['PhysicalResourceId']
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Created new OU: TestOULib'

def test_creating_a_child_ou_should_create_ou():
  f = open('events/ou/create-child.json', 'r')
  global child_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, '', ou_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  child_id = response_json['PhysicalResourceId']
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Created new OU: TestOULibChild'
  
def test_deleting_a_parent_with_child_should_fail_with_exception():
  f = open('events/ou/delete.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'OU has children and cannot be deleted: TestOULib'

def test_cleanup_child():
  f = open('events/ou/delete-child.json', 'r')
  global ou_id
  global child_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, child_id, ou_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Deleted OU: TestOULibChild'
  
def test_cleanup_ou():
  f = open('events/ou/delete.json', 'r')
  global ou_id
  global parent_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("LAMBDA_FUNCTION_NAME"),
    Payload=update_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Deleted OU: TestOULib'
