http --verbose \
    -a $CLIENT_ID:$CLIENT_SECRET \
    --form POST $OAUTH_SERVER/v1/token \
    'Accept:application/json' \
    grant_type=client_credentials scope=myscope
