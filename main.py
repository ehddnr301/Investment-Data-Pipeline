from datetime import datetime, timedelta

from pykrx import stock


def convert_namelist_to_tickerlist(basedate: str, target_name_list: list):
    ticker_list = stock.get_market_ticker_list(basedate)
    ticker_list = [
        ticker
        for ticker in ticker_list
        if stock.get_market_ticker_name(ticker) in target_name_list
    ]

    return ticker_list


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

    ticker_list = convert_namelist_to_tickerlist(BASEDATE, TARGET_NAME_LIST)
