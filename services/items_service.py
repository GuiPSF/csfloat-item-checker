import requests
import pandas as pd
from config import API_KEY, BASE_URL


def get_items() -> pd.DataFrame:
    response = requests.get(
        BASE_URL,
        headers={"Authorization": API_KEY},
        timeout=10,
    )
    response.raise_for_status()

    payload = response.json()
    items = payload.get("data", [])

    return pd.json_normalize(items, sep="_")
