import argparse
from datetime import datetime, timedelta

from prefect import flow

from configs.config import Config
from utils import extract_pykrx, transform_pykrx, load_pykrx


@flow(name="KrxStock_ETL")
def stock_data_etl(basedate):
    ohlcv_df, marketcap_df, netpurchase_df = extract_pykrx(
        basedate,
        Config.TARGET_NAME_LIST,
        Config.DROP_COLUMN_LIST,
        Config.INVESTOR_LIST,
    )
    df = transform_pykrx(ohlcv_df, marketcap_df, netpurchase_df)
    load_pykrx(df, "ods_stock")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--date")
    args = parser.parse_args()
    basedate = args.date or str((datetime.today() + timedelta(hours=9)).date())

    stock_data_etl(basedate)
