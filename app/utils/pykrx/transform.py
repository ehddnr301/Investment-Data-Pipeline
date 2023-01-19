import pandas as pd
from prefect import task

from configs.config import Config


@task(name="KrxStock_Transform")
def transform(ohlcv_df, marketcap_df, netpurchase_df):
    stock_df = pd.merge(
        left=ohlcv_df,
        right=marketcap_df,
        how="left",
        on=["티커"],
    )
    stock_df = pd.merge(left=stock_df, right=netpurchase_df, how="left", on=["티커"])
    stock_df.columns = Config.ENG_COLUMN_NAME

    return stock_df
