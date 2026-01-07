// AWS Amplify Configuration for BMS Customer Lookup - OKTA SAML Only
const awsConfig = {
    Auth: {
        region: 'us-east-1',
        userPoolId: 'us-east-1_RyGcnq6VR',
        userPoolWebClientId: '7mck7388jk5brrc602do008kor',
        oauth: {
            domain: 'bms-customer-lookup-auth.auth.us-east-1.amazoncognito.com',
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
