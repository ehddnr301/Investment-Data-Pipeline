from prefect import flow

from configs.config import Config
from utils.flows import extract, transform, load


@flow(name="KrxStock_ETL")
def stock_data_etl():
    ohlcv_df, marketcap_df, netpurchase_df = extract(
        "2023-01-16",
        Config.TARGET_NAME_LIST,
        Config.DROP_COLUMN_LIST,
        Config.INVESTOR_LIST,
    )
    df = transform(ohlcv_df, marketcap_df, netpurchase_df)
    load(df, "ods_stock")


if __name__ == "__main__":
    stock_data_etl()
