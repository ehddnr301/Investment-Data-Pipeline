from datetime import datetime, timedelta

import pandas as pd
from pykrx import stock


def convert_namelist_to_tickerlist(basedate: str, target_name_list: list):
    ticker_list = stock.get_market_ticker_list(basedate)
    ticker_list = [
        ticker
        for ticker in ticker_list
        if stock.get_market_ticker_name(ticker) in target_name_list
    ]

    return ticker_list


def get_ohlcv(basedate, ticker_list):
    df = pd.DataFrame()
    for tick in ticker_list:
        data = stock.get_market_ohlcv(basedate, basedate, tick)
        data = data.reset_index()
        data.insert(1, "티커", tick)
        df = pd.concat([df, data], ignore_index=True)
    return df


def get_marketcap(basedate, ticker_list):
    df = stock.get_market_cap(basedate)
    df = df.filter(items=ticker_list, axis=0)
    df = df.reset_index()
    return df


def get_net_purchase_by_investor(investor, basedate, ticker_list):
    df = stock.get_market_net_purchases_of_equities(
        basedate, basedate, "KOSPI", investor
    )
    df.drop(columns=["종목명"], inplace=True)
    df = df.filter(items=ticker_list, axis=0)
    df = df.add_prefix(f"{investor}_")
    df = df.reset_index()
    return df


def get_net_purchases_by_investor(basedate, ticker_list, investor_list):
    ticker_dict = {"티커": [tick for tick in ticker_list]}

    df = pd.DataFrame(ticker_dict)
    for investor in investor_list:
        data = get_net_purchase_by_investor(investor, basedate, ticker_list)
        df = pd.merge(left=df, right=data, how="left", on=["티커"])

    return df


if __name__ == "__main__":
    BASEDATE = str((datetime.today() + timedelta(hours=9)).date())
    TARGET_NAME_LIST = [
        "삼성전자",
        "LG에너지솔루션",
        "SK하이닉스",
        "삼성바이오로직스",
        "LG화학",
        "삼성SDI",
        "현대차",
        "NAVER",
        "카카오",
    ]
    INVESTOR_LIST = ["외국인", "금융투자", "투신", "개인"]

    ticker_list = convert_namelist_to_tickerlist(BASEDATE, TARGET_NAME_LIST)

    # Data
    ohlcv_df = get_ohlcv(BASEDATE, ticker_list)
    marketcap_df = get_marketcap(BASEDATE, ticker_list)
    net_purchase_df = get_net_purchases_by_investor(
        BASEDATE, ticker_list, INVESTOR_LIST
    )
