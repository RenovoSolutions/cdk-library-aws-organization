# Creates an OU in an AWS Organization

import boto3
import botocore

def get_ou_id(event):
  organizations = boto3.client('organizations')

  response = organizations.list_organizational_units_for_parent(
      ParentId=event['ResourceProperties']['ParentId']
  )

  for ou in response['OrganizationalUnits']:
    if ou['Name'] == event['ResourceProperties']['Name']:
        return ou['Id']

  raise Exception('OuNotFoundException')

def on_event(event, context):
  print(event)
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event)
  if request_type == 'Update': return on_update(event)
  if request_type == 'Delete': return on_delete(event)
  raise Exception('Invalid request type: {}'.format(request_type))

def on_create(event):
  try:
    print('Creating OU: {}'.format(event['ResourceProperties']['Name']))
    client = boto3.client('organizations')
    response = client.create_organizational_unit(
      ParentId=event['ResourceProperties']['ParentId'],
      Name=event['ResourceProperties']['Name']
    )
    print(response)
    return { 'PhysicalResourceId': response['OrganizationalUnit']['Id'] }
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'DuplicateOrganizationalUnitException':
      print('OU already exists: {}'.format(event['ResourceProperties']['Name']))
      ou_id = get_ou_id(event)
      return {
        'PhysicalResourceId': ou_id,
        'Data': {
          'OuId': ou_id,
          'Name': event['ResourceProperties']['Name']
        }
      }
    
def on_update(event):
  try:
    print('Updating OU: {}'.format(event['ResourceProperties']['Name']))
    client = boto3.client('organizations')
    response = client.update_organizational_unit(
      OrganizationalUnitId=event['PhysicalResourceId'],
      Name=event['ResourceProperties']['Name']
    )
    print(response)
    return {
      'PhysicalResourceId': event['PhysicalResourceId'],
      'Data': {
        'OuId': event['PhysicalResourceId'],
        'Name': event['ResourceProperties']['Name']
      }
    }
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'DuplicateOrganizationalUnitException':
      raise Exception('OU already exists: {}'.format(event['ResourceProperties']['Name']))

def on_delete(event):
  print('Deleting OU: {}'.format(event['ResourceProperties']['Name']))
  client = boto3.client('organizations')
  response = client.delete_organizational_unit(
    OrganizationalUnitId=event['PhysicalResourceId']
  )
  print(response)
  return {
    'PhysicalResourceId': event['PhysicalResourceId'],
    'Data': {
      'OuId': event['PhysicalResourceId'],
      'Name': event['ResourceProperties']['Name']
    }
  }
