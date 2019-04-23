import os
import json
import datetime

import requests
from jwcrypto.jwk import JWK
from jwcrypto.jwt import JWT


raw_token = open('temp-token.txt').read()
jwks_resp = requests.get(os.environ['OAUTH_SERVER'] + '/v1/keys')

first_key = jwks_resp.json()['keys'][0]
key = JWK.from_json(json.dumps(first_key))

# Validate token as per procedure described in:
# https://developer.okta.com/authentication-guide/tokens/validating-id-tokens/#verify-the-claims

# Use built-in claim validation for exact matching
# https://jwcrypto.readthedocs.io/en/latest/jwt.html
expected_claims = {
   "iss": os.environ['OAUTH_SERVER'],
   "aud": os.environ['CLIENT_ID']
}

# Creating JWT object also validates the signature
token = JWT(jwt=raw_token, key=key, check_claims=expected_claims)
claims = json.loads(token.claims)

# Perform issued at and expiration time checks
print('IAT validation: ' + str(datetime.datetime.fromtimestamp(claims['iat']) < datetime.datetime.now()))
print('EXP validation: ' + str(datetime.datetime.fromtimestamp(claims['exp']) > datetime.datetime.now()))
