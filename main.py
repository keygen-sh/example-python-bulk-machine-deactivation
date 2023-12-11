import requests
import sys
import os

if not 'KEYGEN_ACCOUNT_ID' in os.environ:
  print('environment variable KEYGEN_ACCOUNT_ID is required')

  sys.exit(1)

if not 'KEYGEN_LICENSE_ID' in os.environ:
  print('environment variable KEYGEN_LICENSE_ID is required')

  sys.exit(1)

if not 'KEYGEN_LICENSE_KEY' in os.environ:
  print('environment variable KEYGEN_LICENSE_KEY is required')

  sys.exit(1)

# Deactivation will be done in batches of 100.
batch = 1

# Retrieve the latest 100 machines for the license on a loop,
# until all machines are deactivated.
while True:
  res = requests.get(
    'https://api.keygen.sh/v1/accounts/{account}/licenses/{license}/machines?limit={limit}'.format(account=os.environ['KEYGEN_ACCOUNT_ID'], license=os.environ['KEYGEN_LICENSE_ID'], limit=100),
    headers={
      'Authorization': 'License {key}'.format(key=os.environ['KEYGEN_LICENSE_KEY']),
      'Content-Type': 'application/vnd.api+json',
      'Accept': 'application/vnd.api+json'
    }
  ).json()

  # Check for API errors, e.g. authentication issues, or invalid account ID.
  if 'error' in res:
    errors = res['errors']

    print('error: {message}'.format(
      message=map(lambda e: "{} - {}".format(e['title'], e['detail']).lower(), errors),
    ))

    sys.exit(1)

  # Make sure we have at least 1 machine, otherwise we exit to prevent
  # an infinite loop, i.e. this is our base case.
  machines = res['data']

  if len(machines) > 0:
    print('deactivating {count} machines for license {license}... (batch #{batch})'.format(
      license=os.environ['KEYGEN_LICENSE_ID'],
      count=len(machines),
      batch=batch,
    ))
  else:
    print('no machines found for license {license}'.format(
      license=os.environ['KEYGEN_LICENSE_ID'],
    ))

    sys.exit(0)

  # Interate over the machines and deactivate each one.
  for machine in res['data']:
    print('deactivating machine {machine}'.format(
      machine=machine['id'],
    ))

    # Deactivate the machine.
    requests.delete(
      'https://api.keygen.sh/v1/accounts/{account}/machines/{machine}'.format(account=os.environ['KEYGEN_ACCOUNT_ID'], machine=machine['id']),
      headers={
        'Authorization': 'License {key}'.format(key=os.environ['KEYGEN_LICENSE_KEY']),
        'Content-Type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
      }
    )

  # Increment the batch, and repeat.
  batch += 1
