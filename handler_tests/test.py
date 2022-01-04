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

ou_id = ''
child_id = ''
account_id = ''
test_account_name = 'TestAccount'
if 'TEST_ACCOUNT_NAME' in os.environ:
  test_account_name = os.environ['TEST_ACCOUNT_NAME']
test_account_email = ''
if 'TEST_ACCOUNT_EMAIL' in os.environ:
  test_account_email = os.environ['TEST_ACCOUNT_EMAIL']
else:
  raise Exception('TEST_ACCOUNT_EMAIL not set')
test_account_original_ou_id = ''
if 'TEST_ACCOUNT_ORIGINAL_OU' in os.environ:
  test_account_original_ou_id = os.environ['TEST_ACCOUNT_ORIGINAL_OU']
else:
  raise Exception('TEST_ACCOUNT_ORIGINAL_OU not set')
if 'OU_LAMBDA_FUNCTION_NAME' in os.environ:
  print('OU_LAMBDA_FUNCTION_NAME: ' + os.environ['OU_LAMBDA_FUNCTION_NAME'])
else:
  raise Exception('OU_LAMBDA_FUNCTION_NAME not set')
if 'ACCOUNT_LAMBDA_FUNCTION_NAME' in os.environ:
  print('ACCOUNT_LAMBDA_FUNCTION_NAME: ' + os.environ['ACCOUNT_LAMBDA_FUNCTION_NAME'])
else:
  raise Exception('ACCOUNT_LAMBDA_FUNCTION_NAME not set')

def get_root():
  organizations = boto3.client('organizations')
  response = organizations.list_roots()
  return response['Roots'][0]['Id']

parent_id = get_root()

# Updates the payload loaded from the events folder with the ou id created during the tests and the root from the current account
def update_ou_payload(payload, ou, parent_id, update_all_parents=True):
  payload_str = json.load(payload)
  if 'PhysicalResourceId' in payload_str:
    payload_str['PhysicalResourceId'] = ou
  payload_str['ResourceProperties']['Parent'] = parent_id
  if 'OldResourceProperties' in payload_str and update_all_parents:
    payload_str['OldResourceProperties']['Parent'] = parent_id
  payload_bytes_arr = bytes(json.dumps(payload_str), encoding="utf8")
  print('PAYLOAD: ' + json.dumps(payload_str))
  return payload_bytes_arr

def update_account_payload(payload, account_id, account_name, account_email, ou_id, old_ou_id, update_all_props=False):
  payload_str = json.load(payload)
  if 'PhysicalResourceId' in payload_str:
    payload_str['PhysicalResourceId'] = account_id
  payload_str['ResourceProperties']['Email'] = account_email
  payload_str['ResourceProperties']['Name'] = account_name
  if update_all_props:
    payload_str['OldResourceProperties']['Name'] = account_name
    payload_str['OldResourceProperties']['Email'] = account_email
  if 'OldResourceProperties' in payload_str:
    payload_str['OldResourceProperties']['Parent'] = old_ou_id
  payload_str['ResourceProperties']['Parent'] = ou_id
  payload_bytes_arr = bytes(json.dumps(payload_str), encoding="utf8")
  print('PAYLOAD: ' + json.dumps(payload_str))
  return payload_bytes_arr

def test_create_with_import_should_create_or_import_ou():
  global ou_id
  f = open('events/ou/create-with-import.json', 'r')
  global parent_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, '', parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  ou_id = response_json['PhysicalResourceId']
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  
  assert response_json['Data']['Message'] == 'Created new OU: TestOULib' or 'Imported existing OU with same properties: ou-' in response_json['Data']['Message']

def test_create_without_import_should_fail_to_create_ou_with_exception():
  f = open('events/ou/create-no-import.json', 'r')
  global parent_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, '', parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'OU already exists: TestOULib'
  
def test_delete_should_delete_ou():
  f = open('events/ou/delete.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Deleted OU: TestOULib'
  
def test_delete_again_should_notify_ou_already_deleted():
  f = open('events/ou/delete.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'OU has already been deleted: TestOULib'
  
def test_update_ou_when_deleted_should_fail_with_exception():
  f = open('events/ou/update.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'The OU you are trying to update, TestOULib, does not exist.'
  
def test_update_ou_with_recreate_should_create_when_old_does_not_exist():
  f = open('events/ou/update-with-recreate.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, ou_id, parent_id)
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
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, '', ou_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  child_id = response_json['PhysicalResourceId']
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Created new OU: TestOULibChild'
  
def test_deleting_a_parent_ou_with_child_ou_should_fail_with_exception():
  f = open('events/ou/delete.json', 'r')
  global parent_id
  global ou_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'OU has children and cannot be deleted: TestOULib'
  
def test_changing_an_ou_parent_should_fail_with_exception():
  f = open('events/ou/update-parent.json', 'r')
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=f
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'OU parent changed. Organizations does not support moving an OU'
  
def test_creating_or_importing_account_should_fail_if_existing_is_in_another_ou_and_move_disabled():
  f = open('events/account/create-with-import.json', 'r')
  global child_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, '', test_account_name, test_account_email, child_id, test_account_original_ou_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert 'Account already exists, but in a different OU, will NOT import' in response_json['errorMessage']

def test_creating_or_importing_account_should_move_existing_during_import_with_move_enabled_or_create_new():
  f = open('events/account/create-with-import-and-move.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, '', test_account_name, test_account_email, child_id, test_account_original_ou_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  account_id = response_json['PhysicalResourceId']
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert 'Account created with id' in response_json['Data']['Message'] or 'Account moved from' in response_json['Data']['Message']

def test_create_account_with_no_import_should_fail_with_exception():
  f = open('events/account/create-no-import.json', 'r')
  global child_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, '', test_account_name, test_account_email, child_id, test_account_original_ou_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert 'Account already exists, will NOT import' in response_json['errorMessage']

def test_changing_account_email_should_fail_with_exception():
  f = open('events/account/change-email.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, 'TestAccount', 'testing@example.com', child_id, child_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'Cannot update account email. You must update the account email manually.'
  
def test_changing_account_name_should_fail_with_exception():
  f = open('events/account/change-name.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, 'TestAccount', 'testing@example.com', child_id, child_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'Cannot update account name. You must update the account name manually.'
  
def test_changing_account_email_should_succeed_when_its_already_changed():
  f = open('events/account/change-email.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, test_account_name, test_account_email, child_id, child_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['EmailChange'] == 'Email has already been updated. No action required.'
  
def test_changing_account_name_should_succeed_when_its_already_changed():
  f = open('events/account/change-name.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, test_account_name, test_account_email, child_id, child_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['NameChange'] == 'Account name has already been updated. No action required.'
  
def test_moving_account_when_already_moved_should_succeed_with_message():
  f = open('events/account/move-with-disable.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, test_account_name, test_account_email, child_id, 'r-a1b2', update_all_props=True)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['MoveInfo'] == 'Account is already in the expected OU. No action required.'
  
def test_moving_account_with_disable_should_fail_with_exception():
  f = open('events/account/move-with-disable.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, test_account_name, test_account_email, 'r-a1b2', 'r-a1b3', update_all_props=True)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'Account needs to move OUs, but moving OUs is not allowed for this account.'
  
def test_moving_account_with_allow_should_succeed_with_message():
  f = open('events/account/move-with-allow.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, test_account_name, test_account_email, test_account_original_ou_id, child_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['MoveInfo'] == 'Account moved from {} to {}'.format(child_id, test_account_original_ou_id)

def test_delete_account_with_disable_should_raise_exception():
  f = open('events/account/delete-with-disable.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, test_account_name, test_account_email, child_id, test_account_original_ou_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['errorMessage'] == 'AWS does not allow deleting of accounts programmatically and removing this account as a resource is disabled by DisableDelete.'
  
def test_delete_account_should_return_response_about_cant_delete_but_will_remove_resource():
  f = open('events/account/delete.json', 'r')
  global child_id
  global account_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("ACCOUNT_LAMBDA_FUNCTION_NAME"),
    Payload=update_account_payload(f, account_id, test_account_name, test_account_email, child_id, test_account_original_ou_id)
  )
  
  response_json = json.loads(response["Payload"].read())
  print(response_json)
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'AWS does not allow deleting of accounts programmatically, but this account will be removed as a resource: {}'.format(account_id)

def test_cleanup_child():
  f = open('events/ou/delete-child.json', 'r')
  global ou_id
  global child_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, child_id, ou_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Deleted OU: TestOULibChild'
  
def test_cleanup_ou():
  f = open('events/ou/delete.json', 'r')
  global ou_id
  global parent_id
  response = lambda_client.invoke(
    FunctionName=os.getenv("OU_LAMBDA_FUNCTION_NAME"),
    Payload=update_ou_payload(f, ou_id, parent_id)
  )

  response_json = json.loads(response["Payload"].read())
  assert response['ResponseMetadata']['HTTPStatusCode'] == 200
  assert response_json['Data']['Message'] == 'Deleted OU: TestOULib'
