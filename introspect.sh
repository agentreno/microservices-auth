http --verbose \
    -a $CLIENT_ID:$CLIENT_SECRET \
    --form POST $OAUTH_SERVER/instropect \
    token=$TOKEN token_type_hint=access_token
