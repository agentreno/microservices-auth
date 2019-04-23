http --verbose \
    -a $CLIENT_ID:$CLIENT_SECRET \
    --form POST $OAUTH_SERVER/v1/token \
    grant_type=password username=test password=valid scope=profile
