import pandas as pd
from prefect import task


@task(name="KrxStock_Transform")
def transform(ohlcv_df, marketcap_df, netpurchase_df):
    stock_df = pd.merge(
        left=ohlcv_df,
        right=marketcap_df,
        how="left",
        on=["티커"],
    )
    stock_df = pd.merge(left=stock_df, right=netpurchase_df, how="left", on=["티커"])

    return stock_df
