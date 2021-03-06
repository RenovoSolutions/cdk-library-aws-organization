import boto3
import botocore
from time import sleep

def get_ou_id(event):
  organizations = boto3.client('organizations')

  response = organizations.list_organizational_units_for_parent(
      ParentId=event['ResourceProperties']['Parent']
  )

  for ou in response['OrganizationalUnits']:
    if ou['Name'] == event['ResourceProperties']['Name']:
        return ou['Id']

  raise Exception('OuNotFoundException')

def check_for_required_prop(event, prop):
  if prop not in event['ResourceProperties']:
    raise Exception('Required property not found: {}'.format(prop))

def on_event(event, context):  
  print(event)
  check_for_required_prop(event, 'Name')
  check_for_required_prop(event, 'Parent')
  allow_recreate_on_update = False
  import_on_duplicate = False
  try:
    allow_recreate_on_update = True if event['ResourceProperties']['AllowRecreateOnUpdate'] == "true" else False
  except KeyError:
    print('No AllowRecreateOnUpdate property found. Defaulting to false')
  try:
    import_on_duplicate = True if event['ResourceProperties']['ImportOnDuplicate'] == "true" else False
  except KeyError:
    print('No ImportOnDuplicate property found. Defaulting to false')

  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event, import_on_duplicate)
  if request_type == 'Update': return on_update(event, allow_recreate_on_update, import_on_duplicate)
  if request_type == 'Delete': return on_delete(event)
  raise Exception('Invalid request type: {}'.format(request_type))

def on_create(event, import_on_duplicate=False):
  try:
    print('Creating OU: {}'.format(event['ResourceProperties']['Name']))
    client = boto3.client('organizations')
    retries = 10
    tries = 1
    while tries <= retries:
      try:
        response = client.create_organizational_unit(
          ParentId=event['ResourceProperties']['Parent'],
          Name=event['ResourceProperties']['Name']
        )
        break
      except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConcurrentModificationException':
          print('ConcurrentModificationException while creating {}, retrying... ({}/{})'.format(event['ResourceProperties']['Name'], tries, retries))
          sleep(2)
          tries += 1
          if tries > retries:
            raise e
          continue
        else:
          raise e
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
        raise Exception('OU already exists: {}'.format(event['ResourceProperties']['Name']))
    else:
      raise e
    
def on_update(event, recreate_on_update=False, import_on_duplicate=False):
  if event['ResourceProperties']['Parent'] != event['OldResourceProperties']['Parent']:
    print('Parent changed for UO and OUs cant be moved: Was {}. Now {}'.format(event['OldResourceProperties']['Parent'], event['ResourceProperties']['Parent']))
    raise Exception('OU parent changed. Organizations does not support moving an OU')
  try:
    print('Updating OU: {} ({})'.format(event['OldResourceProperties']['Name'], event['PhysicalResourceId']))
    client = boto3.client('organizations')
    retries = 10
    tries = 1
    while tries <= retries:
      try:
        client.update_organizational_unit(
          OrganizationalUnitId=event['PhysicalResourceId'],
          Name=event['ResourceProperties']['Name']
        )
        break
      except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConcurrentModificationException':
          print('ConcurrentModificationException while trying to update {}. Retrying... ({}/{})'.format(event['PhysicalResourceId'], tries, retries))
          sleep(2)
          tries += 1
          if tries > retries:
            raise e
          continue
        else:
          raise e
    
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
      raise Exception('The changes you made to your OU, {}, match another OU that already exists.'.format(event['ResourceProperties']['Name']))
    if e.response['Error']['Code'] == 'OrganizationalUnitNotFoundException':
      if recreate_on_update:
        return on_create(event, import_on_duplicate)
      else:
        raise Exception('The OU you are trying to update, {}, does not exist.'.format(event['OldResourceProperties']['Name']))
    else:
      raise e

def on_delete(event):
  try:
    print('Deleting OU: {}'.format(event['ResourceProperties']['Name']))
    client = boto3.client('organizations')
    retries = 10
    tries = 1
    while tries <= retries:
      try:
        client.delete_organizational_unit(
          OrganizationalUnitId=event['PhysicalResourceId']
        )
        break
      except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConcurrentModificationException':
          print('ConcurrentModificationException while trying to delete {}. Retrying... ({}/{})'.format(event['PhysicalResourceId'], tries, retries))
          sleep(2)
          tries += 1
          if tries > retries:
            raise e
          continue
        else:
          raise e
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
    if e.response['Error']['Code'] == 'OrganizationalUnitNotEmptyException':
      raise Exception('OU has children and cannot be deleted: {}'.format(event['ResourceProperties']['Name']))
    else:
      raise e
