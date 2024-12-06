import requests
import pandas as pd

input_file = r"C:\Users\07nav\Downloads\upstoxbaji2\ohlc-input.xlsx"
df = pd.read_excel(input_file)
# Fetch the top 20 rows from the 'ISIN' column
top_ISIN = df["InstrumentKeyName"].head(20)
top_name = df["Name"].head(20)
instrument_keys = top_ISIN.tolist()
instrument_name = top_name.tolist()
print(instrument_keys)

access_token = open("access_token.txt", "r").read().strip()
# quote = 'https://api.upstox.com/v2/historical-candle/NSE_EQ|INE040A01034/month/2023-12-31/2023-01-01' #to-date/from-date
# quote='https://api-v2.upstox.com/market-quote/ohlc'
headers = {
    "accept": "application/json",
    "Api-Version": "2.0",
    "Authorization": f"Bearer {access_token}",
}
out = []
toDateFromDate = "2024-11-30/2022-01-01"

# Calling API for each instrument and appending to out[]
for i in instrument_keys:
    quote = (
        "https://api.upstox.com/v2/historical-candle/NSE_EQ|"
        + i
        + "/month/"+toDateFromDate
    )  # to-date/from-date
    print("instrument: ", i)
    response = requests.get(quote, headers=headers)
    # Parse the JSON response
    response_data = response.json()
    candles = response_data.get("data", {}).get("candles", [])
    print(f"candles for {i}: {candles}")
    # Append each candle data with the instrument key as a new row
    for candle in candles:
        out.append([i] + candle)
    print("out: ", out)

# Create a DataFrame
columns = ["instrument", "timestamp", "open", "high", "low", "close", "volume", "unknown"]
df_out = pd.DataFrame(out, columns=columns)
# Select the relevant columns
df_out = df_out[["instrument", "timestamp", "open", "high", "low", "close"]]

# Write to an Excel file
output_file = r"C:\Users\07nav\Downloads\upstoxbaji2\ohlc-output.xlsx"
df_out.to_excel(output_file, index=False)
print(f"Data written to {output_file}")
