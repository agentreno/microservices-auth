# microservices-auth

## Description

An example microservices setup using technologies like OIDC and OAuth2 to
manage authn/authz. Uses
[authlib](https://github.com/authlib/example-oauth2-server) and
[httpie](https://httpie.org/doc)

## Installing

Create and activate a python3 virtualenv, `pip install -r
example-oauth2-server/requirements.txt` then run:

- `cd example-oauth2-server`
- `flask initdb`
- `flask run`

Create a client at `http://localhost:5000` then use `test_grant.sh` to initiate
a flow.
