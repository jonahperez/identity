import requests
import json
from ConnectionSettings import *
 
body = {
    'grant_type': 'client_credentials',
    'client_id': app_client_id,
    'client_secret': app_client_secret,
    'scope': 'food_training/food'
}
 
response = requests.post(TOKEN_ENDPOINT, data=body)
token = json.loads(response.text)['access_token']

response = requests.post(API_ENDPOINT, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=utf-8" })
print(response.text)

# use the following command to get the app-client-secret:
# aws cognito-idp describe-user-pool-client --user-pool-id <user-pool-id> --client-id client-id --query UserPoolClient.ClientSecret