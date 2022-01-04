import boto3
import time

def search_ou_for_account(ou, name, email):
  client = boto3.client('organizations')
  print(f'Looking for account ({name}) in OU: {ou["Name"]}')
  accounts = client.list_accounts_for_parent(
    ParentId=ou['Id']
  )['Accounts']

  for account in accounts:
    if account['Name'] == name and account['Email'] == email:
      return [account['Id'], ou['Id'], ou['Name']]
    
  ous = client.list_organizational_units_for_parent(
    ParentId=ou['Id']
  )['OrganizationalUnits']

  if len(ous) > 0:
    print(f'Found {len(ous)} child OUs, will search children for account ({name})')
    for ou in ous:
      result = search_ou_for_account(ou, name, email)
      if result:
        return result

  return None

def get_account_id(name, email):
    client = boto3.client('organizations')

    response = client.list_roots()
    for root in response['Roots']:
      print(f'Collecting OUs from root: {root["Name"]} ({root["Id"]})')
      ous = client.list_organizational_units_for_parent(
        ParentId=root['Id']
      )['OrganizationalUnits']

      print(f'Found {len(ous)} OUs')

      print(f'Searching ous...')
      for ou in ous:
        result = search_ou_for_account(ou, name, email)
        if result:
          return result

      print(f'Looking for account ({name}) in root: {root["Id"]} ({root["Name"]})')
      accounts = client.list_accounts_for_parent(
        ParentId=root['Id']
      )['Accounts']

      for account in accounts:
          if account['Name'] == name and account['Email'] == email:
              return [account['Id'], root, root['Name']]

    raise Exception('AccountNotFoundException')
  
def check_account_creation_status(create_id):
  client = boto3.client('organizations')

  return client.describe_create_account_status(
      CreateAccountRequestId=create_id
  )['CreateAccountStatus']
  
def move_account(account_id, source_ou, destination_ou):
  print('Will move account ({}) from {} to {}'.format(account_id, source_ou, destination_ou))
  client = boto3.client('organizations')
  client.move_account(
    AccountId=account_id,
    SourceParentId=source_ou,
    DestinationParentId=destination_ou
  )
  return 'Account moved from {} to {}'.format(source_ou, destination_ou)

def on_event(event, context):
  import_on_duplicate = True if event['ResourceProperties']['ImportOnDuplicate'] == "true" else False
  allow_move = True if event['ResourceProperties']['AllowMove'] == "true" else False
  disable_delete = True if event['ResourceProperties']['DisableDelete'] == "true" else False

  print(event)
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event, import_on_duplicate, allow_move)
  if request_type == 'Update': return on_update(event, allow_move)
  if request_type == 'Delete': return on_delete(event, disable_delete)
  raise Exception('Invalid request type: {}'.format(request_type))

def on_create(event, import_on_duplicate=False, allow_move=False):
  try:
    existing_account_info = get_account_id(event['ResourceProperties']['Name'], event['ResourceProperties']['Email'])
    if import_on_duplicate:
      if existing_account_info[1] == event['ResourceProperties']['Parent']:
        msg = 'Imported existing account with same properties: {}'.format(existing_account_info[0])
        print(msg)
        return {
          'PhysicalResourceId': existing_account_info[0],
          'Data': {
            'Message': msg
          }
        }
      else:
        if allow_move:
          print('Account already exists, but in a different OU, moving it to the new OU: {} existing in {}({})'.format(existing_account_info[0], existing_account_info[2], existing_account_info[1]))
          msg = move_account(existing_account_info[0], existing_account_info[1], event['ResourceProperties']['Parent'])
          return {
            'PhysicalResourceId': existing_account_info[0],
            'Data': {
              'Message': msg
            }
          }
        else:
          raise Exception('Account already exists, but in a different OU, will NOT import: {} exists in {} ({})'.format(existing_account_info[0], existing_account_info[2], existing_account_info[1]))
    else:
      raise Exception('Account already exists, will NOT import: {} exists in {} ({})'.format(existing_account_info[0], existing_account_info[2], existing_account_info[1]))
  except Exception as e:
    if e == 'AccountNotFoundException':
      print('No existing account found with these properties ({}, {}), sending new account creation request'.format(event['ResourceProperties']['Name'], event['ResourceProperties']['Email']))
      client = boto3.client('organizations')
      response = client.create_account(
        Email=event['ResourceProperties']['Email'],
        AccountName=event['ResourceProperties']['Name'],
      )
      creation_id = response['CreateAccountStatus']['Id']
      create_status = check_account_creation_status(creation_id)
      while create_status['State'] == 'IN_PROGRESS':
        print(f'Waiting for account creation request ({response["CreateAccountStatus"]["Id"]}) to finish. (Sleeping 5 seconds)')
        time.sleep(5)
        create_status = check_account_creation_status(creation_id)
          
      if create_status['State'] == 'FAILED':
        raise Exception('Account creation failed: {}'.format(create_status["FailureReason"]))
      if create_status['State'] == 'SUCCEEDED':
        print('Account created: {}'.format(create_status["AccountId"]))
        print('Moving account to OU: {}'.format(event["ResourceProperties"]["Parent"]))
        roots = client.list_roots()['Roots']
        for root in roots:
          if root['Id'] == event['ResourceProperties']['Parent']:
            print('Account already in expected OU: {} ({})'.format(root["Name"], root["Id"]))
          else:
            response = client.move_account(
              AccountId=create_status['AccountId'],
              SourceParentId=root['Id'],
              DestinationParentId=event['ResourceProperties']['Parent']
            )
            print('Account moved to OU: {} ({})'.format(root["Name"], root["Id"]))
            msg = 'Account created with id {} and moved to OU {}'.format(create_status['AccountId'], root["Id"])
            print(msg)
            return {
              'PhysicalResourceId': create_status['AccountId'],
              'Data': {
                'Message': msg
              }
            }
      raise Exception(f'Unknown account creation status: {create_status["State"]}')
    else:
      raise e
      
def on_update(event, allow_move=False):
  client = boto3.client('organizations')
  account_info = client.describe_account(
    AccountId=event['PhysicalResourceId']
  )
  data = {
    'Message': 'Account has been updated',
    'MoveInfo': 'Account not moved.',
    'NameChange': 'Account name not changed.',
    'EmailChange': 'Account email not changed.'
  }
  if event['OldResourceProperties']['Name'] != event['ResourceProperties']['Name']:
    if account_info['Account']['Name'] == event['ResourceProperties']['Name']:
      data['NameChange'] = 'Account name has already been updated. No action required.'
    else:
      raise Exception('Cannot update account name. You must update the account name manually.')
  if event['OldResourceProperties']['Email'] != event['ResourceProperties']['Email']:
    if account_info['Account']['Email'] == event['ResourceProperties']['Email']:
      data['EmailChange'] = 'Email has already been updated. No action required.'
    else:
      raise Exception('Cannot update account email. You must update the account email manually.')
  account_id_and_location = get_account_id(event['ResourceProperties']['Name'], event['ResourceProperties']['Email'])
  if event['OldResourceProperties']['Parent'] != event['ResourceProperties']['Parent']:
    if account_id_and_location[1] == event['ResourceProperties']['Parent']:
      data['MoveInfo'] = 'Account is already in the expected OU. No action required.'
    else:
      if allow_move:
        data['MoveInfo'] = move_account(account_id_and_location[0], account_id_and_location[1], event['ResourceProperties']['Parent'])
      else:
        raise Exception('Account needs to move OUs, but moving OUs is not allowed for this account.')
  return {
    'PhysicalResourceId': account_id_and_location[0],
    'Data': data
  }

def on_delete(event, disable_delete=False):
  if disable_delete:
    raise Exception('AWS does not allow deleting of accounts programmatically and removing this account as a resource is disabled by DisableDelete.')
  else:
    msg = 'AWS does not allow deleting of accounts programmatically, but this account will be removed as a resource: {}'.format(event['PhysicalResourceId'])
    return {
      'PhysicalResourceId': event['PhysicalResourceId'],
      'Data': {
        'Message': msg
      }
    }