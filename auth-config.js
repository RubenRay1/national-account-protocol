// AWS Amplify Configuration for BMS Customer Lookup - OKTA SAML Only
const awsConfig = {
    Auth: {
        region: 'us-east-1',
        userPoolId: 'us-east-1_6K0VXKjt1',
        userPoolWebClientId: '7si5kk2t9t24nrtgkumc2n6ops',
        oauth: {
            domain: 'national-account-protocol.auth.us-east-1.amazoncognito.com',
            scope: ['email', 'openid', 'profile'],
            redirectSignIn: window.location.origin + '/',
            redirectSignOut: window.location.origin + '/',
            responseType: 'code',
            // Force OKTA SAML login only
            identityProviders: ['SAML']
        }
    }
};

// Configure Amplify
if (typeof Amplify !== 'undefined') {
    Amplify.configure(awsConfig);
}
