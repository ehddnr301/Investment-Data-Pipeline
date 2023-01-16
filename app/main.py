# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

import pandas as pd
from pykrx import stock
from sqlalchemy import create_engine

from configs.config import Config
from utils.pykrx_func import (
    convert_namelist_to_tickerlist,
    get_ohlcv,
    get_marketcap,
    get_net_purchases_by_investor,
)

if __name__ == "__main__":
    BASEDATE = str((datetime.today() + timedelta(hours=9)).date())

    # Extract Data
    ticker_list = convert_namelist_to_tickerlist(BASEDATE, Config.TARGET_NAME_LIST)
    ohlcv_df = get_ohlcv(BASEDATE, ticker_list)
    marketcap_df = get_marketcap(BASEDATE, ticker_list, Config.DROP_COLUMN_LIST)
    net_purchase_df = get_net_purchases_by_investor(
        BASEDATE, ticker_list, Config.INVESTOR_LIST
    )

    # Transform Data
    final_df = pd.merge(
        left=ohlcv_df,
        right=marketcap_df,
        how="left",
        on=["티커"],
    )
    final_df = pd.merge(left=final_df, right=net_purchase_df, how="left", on=["티커"])

    # Load Data
    engine = create_engine(Config.POSTGRES_URL)

    with engine.begin() as conn:
        final_df.to_sql("ods_stock", con=conn, index=False)
