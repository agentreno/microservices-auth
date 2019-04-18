http --verbose \
    -a $CLIENT_ID:$CLIENT_SECRET \
    --form POST http://localhost:5000/oauth/token \
    grant_type=password username=test password=valid scope=profile
