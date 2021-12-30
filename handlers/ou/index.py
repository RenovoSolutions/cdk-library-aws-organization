import boto3
import botocore

def get_ou_id(event):
  organizations = boto3.client('organizations')

  response = organizations.list_organizational_units_for_parent(
      ParentId=event['ResourceProperties']['Parent']
  )

  for ou in response['OrganizationalUnits']:
    if ou['Name'] == event['ResourceProperties']['Name']:
        return ou['Id']

  raise Exception('OuNotFoundException')

def on_event(event, context):  
  print(event)
  allow_merge_on_move = True if event['ResourceProperties']['AllowMergeOnMove'] == "true" else False
  allow_recreate_on_update = True if event['ResourceProperties']['AllowRecreateOnUpdate'] == "true" else False
  import_on_duplicate = True if event['ResourceProperties']['ImportOnDuplicate'] == "true" else False

  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event, allow_merge_on_move, allow_recreate_on_update, import_on_duplicate)
  if request_type == 'Update': return on_update(event, allow_merge_on_move, allow_recreate_on_update, import_on_duplicate)
  if request_type == 'Delete': return on_delete(event)
  raise Exception('Invalid request type: {}'.format(request_type))

def on_create(event, allow_merge_on_move=False, recreate_on_update=False, import_on_duplicate=False):
  try:
    print('Creating OU: {}'.format(event['ResourceProperties']['Name']))
    client = boto3.client('organizations')
    response = client.create_organizational_unit(
      ParentId=event['ResourceProperties']['Parent'],
      Name=event['ResourceProperties']['Name']
    )
    msg = 'Created new OU: {}'.format(event['ResourceProperties']['Name'])
    print(msg)
    print('OU id is: {}'.format(response['OrganizationalUnit']['Id']))
    return {
      'PhysicalResourceId': response['OrganizationalUnit']['Id'],
      'Data': {
        'Message': msg
      }
    }
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'DuplicateOrganizationalUnitException':
      print('OU already exists: {}'.format(event['ResourceProperties']['Name']))
      if import_on_duplicate:
        ou_id = get_ou_id(event)
        msg = 'Imported existing OU with same properties: {}'.format(ou_id)
        print(msg)
        return {
          'PhysicalResourceId': ou_id,
          'Data': {
            'Message': msg
          }
        }
      else:
        raise Exception('OU already exists and import is disabled: {}'.format(event['ResourceProperties']['Name']))
    else:
      raise e
    
def on_update(event, allow_merge_on_move=False, recreate_on_update=False, import_on_duplicate=False):
  if event['ResourceProperties']['Parent'] != event['OldResourceProperties']['Parent']:
    print('Parent changed for UO: Was {}. Now {}'.format(event['OldResourceProperties']['Parent'], event['ResourceProperties']['Parent']))
    return on_create(event, allow_merge_on_move, recreate_on_update, import_on_duplicate)
  try:
    print('Updating OU: {} ({})'.format(event['OldResourceProperties']['Name'], event['PhysicalResourceId']))
    client = boto3.client('organizations')
    response = client.update_organizational_unit(
      OrganizationalUnitId=event['PhysicalResourceId'],
      Name=event['ResourceProperties']['Name']
    )
    msg = 'Updated OU: {} ({})'.format(event['ResourceProperties']['Name'], event['PhysicalResourceId'])
    print(msg)
    return {
      'PhysicalResourceId': event['PhysicalResourceId'],
      'Data': {
        'Message': msg
      }
    }
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'DuplicateOrganizationalUnitException':
      raise Exception('The changes you made to your OU, {}, match another OU that already exists and merging is disabled.'.format(event['ResourceProperties']['Name']))
    if e.response['Error']['Code'] == 'OrganizationalUnitNotFoundException':
      if recreate_on_update:
        return on_create(event, allow_merge_on_move, recreate_on_update, import_on_duplicate)
      else:
        raise Exception('The OU you are trying to update, {}, does not exist and creation of missing OUs on update is disabled.'.format(event['OldResourceProperties']['Name']))
    else:
      raise e

def on_delete(event):
  try:
    print('Deleting OU: {}'.format(event['ResourceProperties']['Name']))
    client = boto3.client('organizations')
    client.delete_organizational_unit(
      OrganizationalUnitId=event['PhysicalResourceId']
    )
    msg = 'Deleted OU: {}'.format(event['ResourceProperties']['Name'])
    print(msg)
    return {
      'PhysicalResourceId': event['PhysicalResourceId'],
      'Data': {
        'Message': msg
      }
    }
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'OrganizationalUnitNotFoundException':
      msg = 'OU has already been deleted: {}'.format(event['ResourceProperties']['Name'])
      print(msg)
      return {
        'PhysicalResourceId': event['PhysicalResourceId'],
        'Data': {
          'Message': msg
        }
      }
