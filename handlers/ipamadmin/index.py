import boto3
import botocore
import json
import os
import inspect
import sys

def check_for_required_prop(event, prop):
  if prop not in event['ResourceProperties']:
    raise Exception('Required property not found: {}'.format(prop))

def on_event(event, context):
  print(event)
  print('Using version {} of boto3.'.format(boto3.__version__))
  check_for_required_prop(event, 'DelegatedAdminAccountId')

  print(event)
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event)
  if request_type == 'Update': return on_update(event)
  if request_type == 'Delete': return on_delete(event)
  raise Exception('Invalid request type: {}'.format(request_type))

def on_create(event):
  client = boto3.client('ec2')
  print('Delegating admin account for IPAM: {}'.format(event['ResourceProperties']['DelegatedAdminAccountId']))
  try:
    # requires boto3 1.20.18 https://github.com/boto/boto3/blob/develop/CHANGELOG.rst#12018
    response = client.enable_ipam_organization_admin_account(
      DelegatedAdminAccountId=event['ResourceProperties']['DelegatedAdminAccountId']
    )
    print(json.dumps(response))
    if response['Success'] == True:
      msg = 'IPAM admin account successfully enabled'
      print('msg')
      return {
        'PhysicalResourceId': event['ResourceProperties']['DelegatedAdminAccountId'],
        'Data': {
          'Message': msg
        }
      }
    else:
      raise Exception('IPAM admin account could not be enabled')
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'IpamOrganizationDelegatedAdminLimitExceeded':
      raise Exception('An IPAM delegated admin already exists and you may only specify one.')
    elif e.response['Error']['Code'] == 'IpamOrganizationAccountNotFound':
      raise Exception('The specified account does not belong to your organization.')
    else:
      raise e
  except Exception as e:
    raise e
      
def on_update(event):
  if event['OldResourceProperties']['DelegatedAdminAccountId'] != event['ResourceProperties']['DelegatedAdminAccountId']:
    on_delete({
      'PhysicalResourceId': event['OldResourceProperties']['DelegatedAdminAccountId'],
    })
    return on_create(event)
  else:
    msg = 'No changes detected, delegated admin ID unchanged'
    print(msg)
    return {
      'PhysicalResourceId': event['PhysicalResourceId'],
      'Data': {
        'Message': msg
      }
    }

def on_delete(event):
  client = boto3.client('ec2')
  print('Removing delegation for IPAM admin account: {}'.format(event['PhysicalResourceId']))
  try:
    # requires boto3 1.20.18 https://github.com/boto/boto3/blob/develop/CHANGELOG.rst#12018
    response = client.disable_ipam_organization_admin_account(
      DelegatedAdminAccountId=event['PhysicalResourceId']
    )
    print(json.dumps(response))
    if response['Success'] == True:
      msg = 'IPAM admin account successfully disabled'
      print(msg)
      return {
        'PhysicalResourceId': event['PhysicalResourceId'],
        'Data': {
          'Message': msg
        }
      }
    else:
      raise Exception('IPAM admin account could not be disabled')
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'IpamOrganizationAccountNotRegistered':
      msg = 'No IPAM delegation exists for this organization and only one can exists. Assuming this delegation was already removed.'
      print(msg)
      return {
        'PhysicalResourceId': event['PhysicalResourceId'],
        'Data': {
          'Message': msg
        }
      }
  except Exception as e:
    raise e
      
