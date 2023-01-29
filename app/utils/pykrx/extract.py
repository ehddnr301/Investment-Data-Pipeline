import pandas as pd
from pykrx import stock


def filter_ticker(ticker_list: list, name_list: list):
    ticker_list = [
        ticker
        for ticker in ticker_list
        if stock.get_market_ticker_name(ticker) in name_list
    ]
    return ticker_list


def get_net_purchase_by_investor(investor: str, basedate: str, ticker_list: list):
    df = stock.get_market_net_purchases_of_equities(
        basedate, basedate, "KOSPI", investor
    )
    df.drop(columns=["종목명"], inplace=True)
    df = df.filter(items=ticker_list, axis=0)
    df = df.add_prefix(f"{investor}_")
    df = df.reset_index()

    return df


def get_ticker_list(basedate: str, target_name_list: list):
    ticker_list = stock.get_market_ticker_list(basedate)
    res = filter_ticker(ticker_list, target_name_list)
    return res


def get_ohlcv(basedate: str, ticker_list: list):
    temp = []
    for tick in ticker_list:
        data = stock.get_market_ohlcv(basedate, basedate, tick)
        data = data.reset_index()
        data.insert(1, "티커", tick)
        temp.append(data)
    df = pd.concat(temp, ignore_index=True)
    return df


def get_marketcap(basedate: str, ticker_list: list, drop_col_list: list):
    df = stock.get_market_cap(basedate)
    df = df.filter(items=ticker_list, axis=0)
    df = df.drop(columns=drop_col_list)
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


def extract(
    basedate: str, target_name_list: list, drop_col_list: list, investor_list: list
):
    ticker_list = get_ticker_list(basedate, target_name_list)
    ohlcv_df = get_ohlcv(basedate, ticker_list)
    marketcap_df = get_marketcap(basedate, ticker_list, drop_col_list)
    netpurchase_df = get_net_purchases_by_investor(basedate, ticker_list, investor_list)

    return ohlcv_df, marketcap_df, netpurchase_df
