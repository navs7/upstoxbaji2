import upstox_client
import time
import pandas as pd

instrument_keys = ["NSE_EQ|INE342T07460", "NSE_EQ|INE342T07452"]
access_token = open("access_token.txt").read().strip()
temp = {
   "feeds":{
      "NSE_EQ|INE342T07403":{
         "ff":{
            "marketFF":{
               "ltpc":{
                  "ltp":1020.0,
                  "ltt":"1729239921221",
                  "ltq":"100",
                  "cp":1020.0
               },
               "marketLevel":{
                  "bidAskQuote":[
                     {
                        "bq":16,
                        "bp":1001.0,
                        "bno":1,
                        "aq":150,
                        "ap":1020.0,
                        "ano":1,
                        "bidQ":"16",
                        "askQ":"150"
                     },
                     {
                        "bq":2,
                        "bp":1000.87,
                        "bno":1,
                        "aq":50,
                        "ap":1025.0,
                        "ano":1,
                        "bidQ":"2",
                        "askQ":"50"
                     },
                     {
                        "bq":50,
                        "bp":990.0,
                        "bno":1,
                        "aq":50,
                        "ap":1030.0,
                        "ano":1,
                        "bidQ":"50",
                        "askQ":"50"
                     },
                     {
                        "bq":19,
                        "bp":862.2,
                        "bno":1,
                        "aq":17,
                        "ap":1099.0,
                        "ano":1,
                        "bidQ":"19",
                        "askQ":"17"
                     },
                     {
                        
                     }
                  ]
               },
               "optionGreeks":{
                  
               },
               "marketOHLC":{
                  "ohlc":[
                     {
                        "interval":"1d",
                        "open":1021.0,
                        "high":1021.0,
                        "low":1020.0,
                        "close":1020.0,
                        "volume":200,
                        "ts":"1729189800000",
                        "vol":"200"
                     },
                     {
                        "interval":"I1",
                        "open":1021.0,
                        "high":1021.0,
                        "low":1021.0,
                        "close":1021.0,
                        "ts":"1729239840000"
                     },
                     {
                        "interval":"I1",
                        "open":1020.0,
                        "high":1020.0,
                        "low":1020.0,
                        "close":1020.0,
                        "volume":100,
                        "ts":"1729239900000",
                        "vol":"100"
                     },
                     {
                        "interval":"I30",
                        "open":1021.0,
                        "high":1021.0,
                        "low":1021.0,
                        "close":1021.0,
                        "volume":100,
                        "ts":"1729237500000",
                        "vol":"100"
                     },
                     {
                        "interval":"I30",
                        "open":1020.0,
                        "high":1020.0,
                        "low":1020.0,
                        "close":1020.0,
                        "volume":100,
                        "ts":"1729239300000",
                        "vol":"100"
                     }
                  ]
               },
               "eFeedDetails":{
                  "atp":1020.5,
                  "cp":1020.0,
                  "vtt":"200",
                  "tbq":87.0,
                  "tsq":267.0,
                  "lc":816.0,
                  "uc":1224.0,
                  "yh":1100.0,
                  "yl":838.2,
                  "fp":1020.0,
                  "fv":100
               }
            }
         }
      },
      "NSE_EQ|INE342T07445":{
         "ff":{
            "marketFF":{
               "ltpc":{
                  "ltp":1042.0,
                  "ltt":"1729241996722",
                  "ltq":"3",
                  "cp":1044.0
               },
               "marketLevel":{
                  "bidAskQuote":[
                     {
                        "bq":1,
                        "bp":1032.21,
                        "bno":1,
                        "aq":72,
                        "ap":1042.0,
                        "ano":1,
                        "bidQ":"1",
                        "askQ":"72"
                     },
                     {
                        "bq":10,
                        "bp":1015.0,
                        "bno":1,
                        "aq":50,
                        "ap":1240.0,
                        "ano":1,
                        "bidQ":"10",
                        "askQ":"50"
                     },
                     {
                        "bq":10,
                        "bp":1014.0,
                        "bno":1,
                        "aq":10,
                        "ap":1249.0,
                        "ano":1,
                        "bidQ":"10",
                        "askQ":"10"
                     },
                     {
                        "bq":10,
                        "bp":1013.0,
                        "bno":1,
                        "bidQ":"10"
                     },
                     {
                        "bq":10,
                        "bp":1012.0,
                        "bno":1,
                        "bidQ":"10"
                     }
                  ]
               },
               "optionGreeks":{
                  
               },
               "marketOHLC":{
                  "ohlc":[
                     {
                        "interval":"1d",
                        "open":1044.0,
                        "high":1044.0,
                        "low":1042.0,
                        "close":1042.0,
                        "volume":103,
                        "ts":"1729189800000",
                        "vol":"103"
                     },
                     {
                        "interval":"I1",
                        "open":1044.0,
                        "high":1044.0,
                        "low":1044.0,
                        "close":1044.0,
                        "ts":"1729241880000"
                     },
                     {
                        "interval":"I1",
                        "open":1042.0,
                        "high":1042.0,
                        "low":1042.0,
                        "close":1042.0,
                        "volume":3,
                        "ts":"1729241940000",
                        "vol":"3"
                     },
                     {
                        "interval":"I30",
                        "open":1044.0,
                        "high":1044.0,
                        "low":1044.0,
                        "close":1044.0,
                        "ts":"1729239300000"
                     },
                     {
                        "interval":"I30",
                        "open":1042.0,
                        "high":1042.0,
                        "low":1042.0,
                        "close":1042.0,
                        "volume":3,
                        "ts":"1729241100000",
                        "vol":"3"
                     }
                  ]
               },
               "eFeedDetails":{
                  "atp":1043.94,
                  "cp":1044.0,
                  "vtt":"103",
                  "tbq":82.0,
                  "tsq":132.0,
                  "lc":835.2,
                  "uc":1252.8,
                  "yh":1050.0,
                  "yl":980.0,
                  "fp":1042.0,
                  "fv":3
               }
            }
         }
      }
   },
   "currentTs":"1729243198645"
}
# Creating an empty dictionary
final_askRateQty = {}
# Creating a list to hold the dictionary
out = []

# Function to dynamically create and add a dictionary to the list
def add_dictionary(ISIN, AskRate, AskQty):
    # Creating a dictionary
    new_dict = {
        'ISIN': ISIN,
        'AskRate': AskRate,
        'AskQty': AskQty
    }    
    # Append the new dictionary to the list
    out.append(new_dict)
    return out


def on_message(message):
    # print(message)
    # print(type(message))
    message_dict = temp     # change to 'message' when getting real time data
    # Now you can extract 'bidAskQuote' from message_dict if it exists
    feeds = message_dict.get("feeds", {})
    for feed_key, feed_value in feeds.items():
        bid_ask_quotes = feed_value['ff']['marketFF']['marketLevel'].get('bidAskQuote', [])
        # print(f"BidAskQuotes for {feed_key}: {bid_ask_quotes}")
        for quote in bid_ask_quotes:
            # Extract 'askQ' from each quote (if it exists)
            aq = quote.get('aq', '0.0')  # Default to 'N/A' if 'aq' is not present
            # print(f"askQty: {aq}")
            ap = quote.get('ap', '0.0')
            # print(f"askRate: {ap}")
            add_dictionary(feed_key, ap, aq)
            
    print(f"final op: {out}")
    # Convert the data into a pandas DataFrame for writing into Excel file
    df = pd.DataFrame(out)
    # Specify the path where you want to save the Excel file
    output_file = 'bid_ask_quotes.xlsx'
    # Write the DataFrame to an Excel file
    df.to_excel(output_file, index=False)
    # df.to_excel(output_file, sheet_name='BidAskData', index=False)


def main():
    config = upstox_client.Configuration()
    config.access_token = access_token
    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(config), instrument_keys, "full"
    )
    streamer.on("message", on_message)
    streamer.connect()
    try:
        time.sleep(15)
    finally:
        streamer.disconnect()
        print("Streamer disconnected.")


if __name__ == "__main__":
    main()
