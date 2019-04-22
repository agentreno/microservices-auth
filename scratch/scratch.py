import os
import json

import requests
from jwcrypto.jwk import JWK
from jwcrypto.jwt import JWT


raw_token = open('temp-token.txt').read()
jwks_resp = requests.get(os.environ['OAUTH_SERVER'] + '/keys')

first_key = jwks_resp.json()['keys'][0]
key = JWK.from_json(json.dumps(first_key))

token = JWT(jwt=raw_token, key=key)
