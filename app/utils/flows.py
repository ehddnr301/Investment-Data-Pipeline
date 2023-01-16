import pandas as pd
from pykrx import stock
from prefect import flow, task, get_run_logger
from prefect.task_runners import ConcurrentTaskRunner

from utils.pykrx_func import (
    filter_ticker,
    get_net_purchase_by_investor,
    create_db_connection,
    check_table_exists,
    load_data,
    initial_load_data,
)


@task(name="convert_name_to_ticker")
def get_ticker_list(basedate: str, target_name_list: list):
    ticker_list = stock.get_market_ticker_list(basedate)
    res = filter_ticker(ticker_list, target_name_list)
    return res


@task(name="get_ohlcv")
def get_ohlcv(basedate: str, ticker_list: list):
    temp = []
    for tick in ticker_list:
        data = stock.get_market_ohlcv(basedate, basedate, tick)
        data = data.reset_index()
        data.insert(1, "티커", tick)
        temp.append(data)
    df = pd.concat(temp, ignore_index=True)
    return df


@task(name="get_marketcap")
def get_marketcap(basedate: str, ticker_list: list, drop_col_list: list):
    df = stock.get_market_cap(basedate)
    df = df.filter(items=ticker_list, axis=0)
    df = df.drop(columns=drop_col_list)
    df = df.reset_index()

    return df


@task(name="get_net_purchases_by_investor")
def get_net_purchases_by_investor(
    basedate: str, ticker_list: list, investor_list: list
):
    ticker_dict = {"티커": [tick for tick in ticker_list]}

    df = pd.DataFrame(ticker_dict)
    for investor in investor_list:
        data = get_net_purchase_by_investor(investor, basedate, ticker_list)
        df = pd.merge(left=df, right=data, how="left", on=["티커"])

    return df


@flow(name="KrxStock_Extract", task_runner=ConcurrentTaskRunner)
def extract(
    basedate: str, target_name_list: list, drop_col_list: list, investor_list: list
):
    ticker_list = get_ticker_list(basedate, target_name_list)
    ohlcv_df = get_ohlcv.submit(basedate, ticker_list)
    marketcap_df = get_marketcap.submit(basedate, ticker_list, drop_col_list)
    netpurchase_df = get_net_purchases_by_investor.submit(
        basedate, ticker_list, investor_list
    )

    return ohlcv_df, marketcap_df, netpurchase_df


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


@task(name="KrxStock_Load")
def load(df, table_name):
    # Create Connection
    psycopg_conn = create_db_connection("psycopg")
    sqlalchemy_engine = create_db_connection("sqlalchemy")

    # Check Table Exists
    is_exists = check_table_exists(sqlalchemy_engine, table_name)

    # Load Data
    if is_exists:
        load_data(psycopg_conn, df, table_name)
    else:
        initial_load_data(sqlalchemy_engine, df, table_name)
