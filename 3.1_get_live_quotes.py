import upstox_client
import time
import pandas as pd

input_file = r"C:\Users\07nav\Downloads\upstoxbaji2\ISIN.xlsx"
df = pd.read_excel(input_file)
# Fetch the top 20 rows from the 'ISIN' column
top_ISIN = df['ISIN3'].head(10)
instrument_keys = top_ISIN.tolist()
print(instrument_keys)

# instrument_keys = ['NSE_EQ|INE342T07445']#["NSE_EQ|INE00QS24019", "NSE_EQ|INE00QS24027", "NSE_EQ|INE00QS24035", "NSE_EQ|INE00QS24043", "NSE_EQ|INE00XE07119"]#, "NSE_EQ|INE00XE07143", "NSE_EQ|INE00XE07176", "NSE_EQ|INE00XE07184", "NSE_EQ|INE01CY077B7", "NSE_EQ|INE01CY077C5", "NSE_EQ|INE01CY077D3", "NSE_EQ|INE01CY077E1", "NSE_EQ|INE01CY077F8", "NSE_EQ|INE01CY077G6", "NSE_EQ|INE01CY077H4", "NSE_EQ|INE01CY077I2", "NSE_EQ|INE01CY077J0", "NSE_EQ|INE01CY077K8", "NSE_EQ|INE01CY077L6", "NSE_EQ|INE01CY077M4", "NSE_EQ|INE01CY077N2", "NSE_EQ|INE01CY077O0", "NSE_EQ|INE01CY077P7", "NSE_EQ|INE01CY077Q5", "NSE_EQ|INE01CY077R3", "NSE_EQ|INE01CY077S1", "NSE_EQ|INE01CY077T9", "NSE_EQ|INE01CY077U7", "NSE_EQ|INE01HV07403", "NSE_EQ|INE01HV07411", "NSE_EQ|INE01HV07429", "NSE_EQ|INE01HV07429", "NSE_EQ|INE01HV07437", "NSE_EQ|INE01HV07445", "NSE_EQ|INE01I507091", "NSE_EQ|INE01I507190", "NSE_EQ|INE01I507273", "NSE_EQ|INE01I507281", "NSE_EQ|INE01I507299", "NSE_EQ|INE01I507372", "NSE_EQ|INE01I507380", "NSE_EQ|INE01I507398", "NSE_EQ|INE01I507455", "NSE_EQ|INE01I507463", "NSE_EQ|INE01I507471", "NSE_EQ|INE01I507489", "NSE_EQ|INE01I507497", "NSE_EQ|INE01I507554", "NSE_EQ|INE01I507562", "NSE_EQ|INE01I507570", "NSE_EQ|INE01I507588", "NSE_EQ|INE01I507596", "NSE_EQ|INE01I507638", "NSE_EQ|INE01I507646", "NSE_EQ|INE01I507653", "NSE_EQ|INE01I507661", "NSE_EQ|INE01I507679", "NSE_EQ|INE01I507703", "NSE_EQ|INE01I507729", "NSE_EQ|INE01I507737", "NSE_EQ|INE01I507752", "NSE_EQ|INE01I507778", "NSE_EQ|INE01I507786", "NSE_EQ|INE01I507794", "NSE_EQ|INE01I507802", "NSE_EQ|INE01I507810", "NSE_EQ|INE01I507828", "NSE_EQ|INE01I507836", "NSE_EQ|INE01I507844", "NSE_EQ|INE01I507851", "NSE_EQ|INE01I507869", "NSE_EQ|INE01I507877", "NSE_EQ|INE01I507885", "NSE_EQ|INE01I507935", "NSE_EQ|INE01I507943", "NSE_EQ|INE01I507950", "NSE_EQ|INE01I507968", "NSE_EQ|INE01I507976", "NSE_EQ|INE01I507984", "NSE_EQ|INE01I507992", "NSE_EQ|INE01I507AA8", "NSE_EQ|INE01I507AB6", "NSE_EQ|INE01I507AC4", "NSE_EQ|INE020B07GH7", "NSE_EQ|INE020B07GH7", "NSE_EQ|INE020B07GX4", "NSE_EQ|INE020B07GX4", "NSE_EQ|INE020B07GZ9", "NSE_EQ|INE020B07HP8", "NSE_EQ|INE020B07HP8", "NSE_EQ|INE020B07HS2", "NSE_EQ|INE020B07HS2", "NSE_EQ|INE020B07HT0", "NSE_EQ|INE020B07HT0", "NSE_EQ|INE020B07ID2", "NSE_EQ|INE020B07ID2", "NSE_EQ|INE020B07IE0", "NSE_EQ|INE020B07IE0", "NSE_EQ|INE020B07IG5", "NSE_EQ|INE020B07IG5", "NSE_EQ|INE020B07IH3", "NSE_EQ|INE020B07IH3", "NSE_EQ|INE020B07JP4", "NSE_EQ|INE020B07JQ2", "NSE_EQ|INE020B07JR0", "NSE_EQ|INE020B07JS8", "NSE_EQ|INE020B07JT6", "NSE_EQ|INE020B07JU4", "NSE_EQ|INE020B07JU4", "NSE_EQ|INE020B07JU4", "NSE_EQ|INE027E07964", "NSE_EQ|INE027E07964", "NSE_EQ|INE027E07972", "NSE_EQ|INE027E07972", "NSE_EQ|INE027E07972", "NSE_EQ|INE027E07980", "NSE_EQ|INE027E07980", "NSE_EQ|INE027E07998", "NSE_EQ|INE027E07998", "NSE_EQ|INE027E07998", "NSE_EQ|INE027E07AK3", "NSE_EQ|INE027E07AK3", "NSE_EQ|INE027E07AL1", "NSE_EQ|INE027E07AL1", "NSE_EQ|INE027E07AL1", "NSE_EQ|INE027E07AM9", "NSE_EQ|INE027E07AM9", "NSE_EQ|INE027E07AN7", "NSE_EQ|INE027E07AN7", "NSE_EQ|INE027E07AN7", "NSE_EQ|INE027E07AX6", "NSE_EQ|INE027E07AX6", "NSE_EQ|INE027E07AY4", "NSE_EQ|INE027E07AY4", "NSE_EQ|INE027E07AY4", "NSE_EQ|INE027E07AZ1", "NSE_EQ|INE027E07AZ1", "NSE_EQ|INE027E07BA2", "NSE_EQ|INE027E07BA2", "NSE_EQ|INE027E07BA2", "NSE_EQ|INE027E07BB0", "NSE_EQ|INE027E07BB0", "NSE_EQ|INE027E07BC8", "NSE_EQ|INE027E07BC8", "NSE_EQ|INE027E07BC8", "NSE_EQ|INE031A07840", "NSE_EQ|INE031A07840", "NSE_EQ|INE031A07865", "NSE_EQ|INE031A07865", "NSE_EQ|INE031A07881", "NSE_EQ|INE031A07915", "NSE_EQ|INE031A07915", "NSE_EQ|INE031A07949", "NSE_EQ|INE031A07949", "NSE_EQ|INE031A07972", "NSE_EQ|INE031A07972", "NSE_EQ|INE031A07AB2", "NSE_EQ|INE031A07AB2", "NSE_EQ|INE031A07AL1", "NSE_EQ|INE031A07AM9", "NSE_EQ|INE031A07AN7", "NSE_EQ|INE031A07AO5", "NSE_EQ|INE031A07AO5", "NSE_EQ|INE031A07AO5", "NSE_EQ|INE031A07AQ0", "NSE_EQ|INE031A07AR8", "NSE_EQ|INE031A07AR8", "NSE_EQ|INE031A07AS6", "NSE_EQ|INE031A07AT4", "NSE_EQ|INE031A07AT4", "NSE_EQ|INE031A07AT4", "NSE_EQ|INE033L07GN7", "NSE_EQ|INE033L07GN7", "NSE_EQ|INE033L07GN7", "NSE_EQ|INE033L07GO5", "NSE_EQ|INE033L07GO5", "NSE_EQ|INE033L07GO5", "NSE_EQ|INE033L07GP2", "NSE_EQ|INE033L07GP2", "NSE_EQ|INE033L07GP2", "NSE_EQ|INE033L07GQ0", "NSE_EQ|INE033L07GQ0", "NSE_EQ|INE033L07GQ0", "NSE_EQ|INE033L07GR8", "NSE_EQ|INE033L07GR8", "NSE_EQ|INE033L07GR8", "NSE_EQ|INE033L07GS6", "NSE_EQ|INE033L07GS6", "NSE_EQ|INE033L07GS6", "NSE_EQ|INE033L07GT4", "NSE_EQ|INE033L07GT4", "NSE_EQ|INE033L07GU2", "NSE_EQ|INE033L07GU2", "NSE_EQ|INE033L07GU2", "NSE_EQ|INE033L07IE2", "NSE_EQ|INE033L08270", "NSE_EQ|INE033L08270", "NSE_EQ|INE033L08270", "NSE_EQ|INE039A07801", "NSE_EQ|INE039A07801", "NSE_EQ|INE039A07801", "NSE_EQ|INE039A07819", "NSE_EQ|INE039A07819", "NSE_EQ|INE039A07819", "NSE_EQ|INE039A07843", "NSE_EQ|INE039A07843", "NSE_EQ|INE039A07843", "NSE_EQ|INE039A07850", "NSE_EQ|INE039A07850", "NSE_EQ|INE039A07850", "NSE_EQ|INE03W107215"]
access_token_file = r"C:\Users\07nav\Downloads\upstoxbaji2\access_token.txt"
access_token = open(access_token_file).read().strip()
temp = {
    "feeds": {
        "NSE_EQ|INE342T07403": {
            "ff": {
                "marketFF": {
                    "ltpc": {
                        "ltp": 1020.0,
                        "ltt": "1729239921221",
                        "ltq": "100",
                        "cp": 1020.0,
                    },
                    "marketLevel": {
                        "bidAskQuote": [
                            {
                                "bq": 16,
                                "bp": 1001.0,
                                "bno": 1,
                                "aq": 150,
                                "ap": 1020.0,
                                "ano": 1,
                                "bidQ": "16",
                                "askQ": "150",
                            },
                            {
                                "bq": 2,
                                "bp": 1000.87,
                                "bno": 1,
                                "aq": 50,
                                "ap": 1025.0,
                                "ano": 1,
                                "bidQ": "2",
                                "askQ": "50",
                            },
                            {
                                "bq": 50,
                                "bp": 990.0,
                                "bno": 1,
                                "aq": 50,
                                "ap": 1030.0,
                                "ano": 1,
                                "bidQ": "50",
                                "askQ": "50",
                            },
                            {
                                "bq": 19,
                                "bp": 862.2,
                                "bno": 1,
                                "aq": 17,
                                "ap": 1099.0,
                                "ano": 1,
                                "bidQ": "19",
                                "askQ": "17",
                            },
                            {},
                        ]
                    },
                    "optionGreeks": {},
                    "marketOHLC": {
                        "ohlc": [
                            {
                                "interval": "1d",
                                "open": 1021.0,
                                "high": 1021.0,
                                "low": 1020.0,
                                "close": 1020.0,
                                "volume": 200,
                                "ts": "1729189800000",
                                "vol": "200",
                            },
                            {
                                "interval": "I1",
                                "open": 1021.0,
                                "high": 1021.0,
                                "low": 1021.0,
                                "close": 1021.0,
                                "ts": "1729239840000",
                            },
                            {
                                "interval": "I1",
                                "open": 1020.0,
                                "high": 1020.0,
                                "low": 1020.0,
                                "close": 1020.0,
                                "volume": 100,
                                "ts": "1729239900000",
                                "vol": "100",
                            },
                            {
                                "interval": "I30",
                                "open": 1021.0,
                                "high": 1021.0,
                                "low": 1021.0,
                                "close": 1021.0,
                                "volume": 100,
                                "ts": "1729237500000",
                                "vol": "100",
                            },
                            {
                                "interval": "I30",
                                "open": 1020.0,
                                "high": 1020.0,
                                "low": 1020.0,
                                "close": 1020.0,
                                "volume": 100,
                                "ts": "1729239300000",
                                "vol": "100",
                            },
                        ]
                    },
                    "eFeedDetails": {
                        "atp": 1020.5,
                        "cp": 1020.0,
                        "vtt": "200",
                        "tbq": 87.0,
                        "tsq": 267.0,
                        "lc": 816.0,
                        "uc": 1224.0,
                        "yh": 1100.0,
                        "yl": 838.2,
                        "fp": 1020.0,
                        "fv": 100,
                    },
                }
            }
        },
        "NSE_EQ|INE342T07445": {
            "ff": {
                "marketFF": {
                    "ltpc": {
                        "ltp": 1042.0,
                        "ltt": "1729241996722",
                        "ltq": "3",
                        "cp": 1044.0,
                    },
                    "marketLevel": {
                        "bidAskQuote": [
                            {
                                "bq": 1,
                                "bp": 1032.21,
                                "bno": 1,
                                "aq": 72,
                                "ap": 1042.0,
                                "ano": 1,
                                "bidQ": "1",
                                "askQ": "72",
                            },
                            {
                                "bq": 10,
                                "bp": 1015.0,
                                "bno": 1,
                                "aq": 50,
                                "ap": 1240.0,
                                "ano": 1,
                                "bidQ": "10",
                                "askQ": "50",
                            },
                            {
                                "bq": 10,
                                "bp": 1014.0,
                                "bno": 1,
                                "aq": 10,
                                "ap": 1249.0,
                                "ano": 1,
                                "bidQ": "10",
                                "askQ": "10",
                            },
                            {"bq": 10, "bp": 1013.0, "bno": 1, "bidQ": "10"},
                            {"bq": 10, "bp": 1012.0, "bno": 1, "bidQ": "10"},
                        ]
                    },
                    "optionGreeks": {},
                    "marketOHLC": {
                        "ohlc": [
                            {
                                "interval": "1d",
                                "open": 1044.0,
                                "high": 1044.0,
                                "low": 1042.0,
                                "close": 1042.0,
                                "volume": 103,
                                "ts": "1729189800000",
                                "vol": "103",
                            },
                            {
                                "interval": "I1",
                                "open": 1044.0,
                                "high": 1044.0,
                                "low": 1044.0,
                                "close": 1044.0,
                                "ts": "1729241880000",
                            },
                            {
                                "interval": "I1",
                                "open": 1042.0,
                                "high": 1042.0,
                                "low": 1042.0,
                                "close": 1042.0,
                                "volume": 3,
                                "ts": "1729241940000",
                                "vol": "3",
                            },
                            {
                                "interval": "I30",
                                "open": 1044.0,
                                "high": 1044.0,
                                "low": 1044.0,
                                "close": 1044.0,
                                "ts": "1729239300000",
                            },
                            {
                                "interval": "I30",
                                "open": 1042.0,
                                "high": 1042.0,
                                "low": 1042.0,
                                "close": 1042.0,
                                "volume": 3,
                                "ts": "1729241100000",
                                "vol": "3",
                            },
                        ]
                    },
                    "eFeedDetails": {
                        "atp": 1043.94,
                        "cp": 1044.0,
                        "vtt": "103",
                        "tbq": 82.0,
                        "tsq": 132.0,
                        "lc": 835.2,
                        "uc": 1252.8,
                        "yh": 1050.0,
                        "yl": 980.0,
                        "fp": 1042.0,
                        "fv": 3,
                    },
                }
            }
        },
    },
    "currentTs": "1729243198645",
}
# Creating a list to hold the dictionary
out2 = []
new_dict2 = {}


def on_message(message):
    # print(message)
    # print(type(message))
    message_dict = message  # change to 'message' when getting real time data else 'temp'
    # Now you can extract 'bidAskQuote' from message_dict if it exists
    feeds = message_dict.get("feeds", {})
    for feed_key, feed_value in feeds.items():
        bid_ask_quotes = feed_value["ff"]["marketFF"]["marketLevel"].get(
            "bidAskQuote", []
        )
        print(f"BidAskQuotes for {feed_key}: {bid_ask_quotes} \n")
        new_dict2.update({"ISIN" : feed_key})
        if(bid_ask_quotes == []):
            print("no data from API\n")
            for i in range(5):
                new_dict2.update({f"AskRate{i+1}" : "no data"})
                new_dict2.update({f"AskQty{i+1}" : "no data"})
        else:
            for i in range(5):
                new_dict2.update({f"AskRate{i+1}" : bid_ask_quotes[i].get('ap','0.0')})
                new_dict2.update({f"AskQty{i+1}" : bid_ask_quotes[i].get('aq','0.0')})
        out2.append(new_dict2.copy()) # ********* new_dict2.copy() creates a shallow copy of new_dict2, so out contains an independent copy of the dictionary.
        new_dict2.clear()
    
    print(f"final op:\n {out2}")
    # Convert the data into a pandas DataFrame for writing into Excel file
    df = pd.DataFrame(out2)
    # Specify the path where you want to save the Excel file
    output_file = r"C:\Users\07nav\Downloads\upstoxbaji2\bid_ask_quotes.xlsx"
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
