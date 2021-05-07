import time
import seldon_deploy_sdk
from seldon_deploy_sdk import Configuration, ApiClient,EnvironmentApi
from seldon_deploy_sdk.auth import OIDCAuthenticator

client_id='sd-api'
username = 'admin@seldon.io'
password = '12341234'
scope = 'openid profile email groups'

#This program repeatedly calls the user endpoint
#it outputs the token, which you can put in jwt.io to check the timeout
#the calls continue to work indefinitely as it keeps getting new tokens

def call_env():
    api_client = ApiClient(configuration=config,authenticator=auth)

    env_api = EnvironmentApi(api_client)
    user = env_api.read_user()
    return user

config = Configuration()
config.host = "http://x.x.x.x/seldon-deploy/api/v1alpha1"
config.oidc_client_id = client_id
config.oidc_server = "http://x.x.x.x/auth/realms/deploy-realm"
config.username = username
config.password = password
config.auth_method = 'password_grant'
#to use client credential set above to client_credentials and uncomment and set config.oidc_client_secret
#config.oidc_client_secret = 'xxxxx'
#note client has to be configured in identity provider for client_credentials

auth = OIDCAuthenticator(config)

config.access_token = auth.authenticate()

print(config.access_token)

for i in range(1, 900):
    env = call_env()

    time.sleep(1)
    if i % 30 == 0:
        print(str(i)+"s")
        print(env)
