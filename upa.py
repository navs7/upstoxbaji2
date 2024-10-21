import requests
import upstox_client
# api_key=open('api_key.txt','r').read().strip()
# api_secret=open('api_secret.txt','r').read().strip()
# uri='https://account.upstox.com/developer/apps'
# code='ok4YyM'
# url='https://api-v2.upstox.com/login/authorization/token'
# headers={
#       'accept': 'application/json',
#       'Api-Version': '2.0',
#       'Content-Type': 'application/x-www-form-urlencoded'
#       }
# data={
#     'code':code,
#     'client_id':api_key,
#     'client_secret':api_secret,
#     'redirect_uri':uri,
#     'grant_type':'authorization_code'
#     }
# response=requests.post(url,headers=headers,data=data)
# access_token=response.json()['access_token']
# access_token = ""
# print(access_token,file=open('access_token.txt','w'))
# print("token: "+access_token)
# access_token=open('access_token.txt','r').read().strip()
# print("token: "+access_token)
# quote='https://api-v2.upstox.com/market-quote/quotes?symbol=NSE_EQ|INE342T07403'
# headers={
#   'accept': 'application/json',
#  'Api-Version': '2.0',
#  'Authorization': f'Bearer {access_token}'
#   }
# response=requests.get(quote,headers=headers)
# print(response.json())
#######################################################################################
# import upstox_client
# instrument_keys=['NSE_FO|37054','NSE_INDEX|Nifty 50','NSE_INDEX|Bank Nifty']
instrument_keys=['NSE_EQ|INE342T07403','NSE_EQ|INE342T07445']
access_token=open('access_token.txt').read().strip()
# print("token: "+access_token)
def on_message(message):
    print(message)
def main():
    config=upstox_client.Configuration()
    config.access_token=access_token
    streamer=upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(config),instrument_keys,'full')
    streamer.on('message',on_message)
    streamer.connect()
if __name__=='__main__':
    main()