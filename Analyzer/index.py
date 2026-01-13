import pandas as pd
import requests
import os

api_key = os.environ.get("API_KEY")
base_url = os.environ.get("BASE_URL")


response = requests.get(
    base_url,
    headers={"Authorization": api_key},
)

payload = response.json()
items = payload["data"]

items[0]


df = pd.json_normalize(items, sep="_")
df.info()

x = input("Test: ")

filtro = df["item_market_hash_name"].str.contains(x, case=False, na=False, regex=False)

df.loc[filtro, ["item_market_hash_name", "price"]]
