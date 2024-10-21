import requests

api_key = open("api_key.txt", "r").read().strip()
rurl = "https://account.upstox.com/developer/apps"
uri = f"https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={ api_key }&redirect_uri={rurl}"
print(uri)
