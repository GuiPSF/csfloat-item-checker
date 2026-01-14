import pandas as pd


def build_filter(df: pd.DataFrame, item_name: str) -> pd.Series:
    return df["item_market_hash_name"].str.contains(
        item_name, case=False, na=False, regex=False
    )


def build_filtered_df(df: pd.DataFrame, mask: pd.Series) -> pd.DataFrame:
    return df.loc[mask, ["item_market_hash_name", "price", "id"]]
