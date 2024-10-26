import requests

api_key = open("api_key.txt", "r").read().strip()
api_secret = open("api_secret.txt", "r").read().strip()
uri = "https://account.upstox.com/developer/apps"
############# UPDATE THE 'code' VALUE HERE ####################
code = "cYg8aG"
#############################################################
url = "https://api-v2.upstox.com/login/authorization/token"
headers = {
    "accept": "application/json",
    "Api-Version": "2.0",
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {
    "code": code,
    "client_id": api_key,
    "client_secret": api_secret,
    "redirect_uri": uri,
    "grant_type": "authorization_code",
}
response = requests.post(url, headers=headers, data=data)
access_token = response.json()["access_token"]
print(
    access_token, file=open("access_token.txt", "w")
)  # write 'access-token' to txt file
print("token: "+access_token)
