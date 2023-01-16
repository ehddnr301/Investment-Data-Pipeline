import pandas as pd
from pykrx import stock
import psycopg2
import psycopg2.extras as extras
from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine

from configs.config import Config


def create_psycopg_conn(params_dic):
    conn = None
    try:
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn


def create_db_connection(engine_type: str):
    if engine_type == "psycopg":
        return create_psycopg_conn(
            {
                "host": Config.POSTGRES_HOST,
                "database": Config.POSTGRES_DATABASE,
                "port": Config.POSTGRES_PORT,
                "user": Config.POSTGRES_USER,
                "password": Config.POSTGRES_PASSWORD,
            }
        )
    if engine_type == "sqlalchemy":
        return create_engine(
            "postgresql://{}:{}@{}:{}/{}".format(
                Config.POSTGRES_USER,
                Config.POSTGRES_PASSWORD,
                Config.POSTGRES_HOST,
                Config.POSTGRES_PORT,
                Config.POSTGRES_DATABASE,
            )
        )


def convert_namelist_to_tickerlist(basedate: str, target_name_list: list):
    ticker_list = stock.get_market_ticker_list(basedate)
    ticker_list = [
        ticker
        for ticker in ticker_list
        if stock.get_market_ticker_name(ticker) in target_name_list
    ]

    return ticker_list


def get_ohlcv(basedate: str, ticker_list: list):
    df = pd.DataFrame()
    for tick in ticker_list:
        data = stock.get_market_ohlcv(basedate, basedate, tick)
        data = data.reset_index()
        data.insert(1, "티커", tick)
        df = pd.concat([df, data], ignore_index=True)
    return df


def get_marketcap(basedate: str, ticker_list: list, drop_col_list: list):
    df = stock.get_market_cap(basedate)
    df = df.filter(items=ticker_list, axis=0)
    df = df.reset_index()
    df = df.drop(columns=drop_col_list)
    return df


def get_net_purchase_by_investor(investor: str, basedate: str, ticker_list: list):
    df = stock.get_market_net_purchases_of_equities(
        basedate, basedate, "KOSPI", investor
    )
    df.drop(columns=["종목명"], inplace=True)
    df = df.filter(items=ticker_list, axis=0)
    df = df.add_prefix(f"{investor}_")
    df = df.reset_index()
    return df


def get_net_purchases_by_investor(
    basedate: str, ticker_list: list, investor_list: list
):
    ticker_dict = {"티커": [tick for tick in ticker_list]}

    df = pd.DataFrame(ticker_dict)
    for investor in investor_list:
        data = get_net_purchase_by_investor(investor, basedate, ticker_list)
        df = pd.merge(left=df, right=data, how="left", on=["티커"])

    return df


def check_table_exists(engine: Engine, table_name: str):
    is_exists = engine.has_table(table_name)

    return is_exists


def initial_load_data(engine: Engine, df: pd.DataFrame, table_name: str):
    with engine.begin() as conn:
        df.to_sql(table_name, con=conn, index=False)


def load_data(conn, df, table_name):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ",".join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" % (table_name, cols)
    cursor = conn.cursor()

    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        cursor.close()
        print(error)
    cursor.close()
