const OktaJwtVerifier = require('@okta/jwt-verifier');
const oktaJwtVerifier = new OktaJwtVerifier({
   issuer: '',
   clientId: ''
});

var mytoken = '';
oktaJwtVerifier.verifyAccessToken(mytoken)
.then(jwt => {
   console.log(jwt.claims);
})
.catch(err => {
   console.log('Validation failed');
   console.log(err);
});
