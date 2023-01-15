# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from configs.config import Config
from utils.pykrx_func import (
    convert_namelist_to_tickerlist,
    get_ohlcv,
    get_marketcap,
    get_net_purchases_by_investor,
    insert_data_to_db,
    execute_query,
)
from utils.queries import CREATE_STOCK_QUERY, INSERT_STOCK_QUERY


if __name__ == "__main__":
    BASEDATE = str((datetime.today() + timedelta(hours=9)).date())

    # Extract Data
    ticker_list = convert_namelist_to_tickerlist(BASEDATE, Config.TARGET_NAME_LIST)

    ohlcv_df = get_ohlcv(BASEDATE, ticker_list)
    marketcap_df = get_marketcap(BASEDATE, ticker_list)
    net_purchase_df = get_net_purchases_by_investor(
        BASEDATE, ticker_list, Config.INVESTOR_LIST
    )

    # Load Data
    insert_data_to_db(ohlcv_df, "ods_ohlcv")
    insert_data_to_db(marketcap_df, "ods_marketcap")
    insert_data_to_db(net_purchase_df, "ods_netpurchase")

    execute_query(CREATE_STOCK_QUERY)
    execute_query(INSERT_STOCK_QUERY)
