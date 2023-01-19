import os
from dotenv import load_dotenv
from typing import List

load_dotenv()


class Config:
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT")
    POSTGRES_DATABASE: str = os.getenv("POSTGRES_DATABASE")

    BIGQUEY_PROJECT_ID: str = os.getenv("BIGQUEY_PROJECT_ID")
    BIGQUEY_DATASET_NAME: str = os.getenv("BIGQUEY_DATASET_NAME")

    TARGET_NAME_LIST: List[str] = [
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
    INVESTOR_LIST: List[str] = ["외국인", "금융투자", "투신", "개인"]
    DROP_COLUMN_LIST: List[str] = ["종가", "거래량", "거래대금"]

    # fmt: off
    ENG_COLUMN_NAME: List[str] = [
        "basedate", "ticker", "open_price", "high_price", "low_price", "close_price","volume","transaction_price","decrease_rate","market_capitalization",
        'Number_of_listed_stocks','Foreigner_sold_transaction_volume','Foreigner_purchase_transaction_volume','Foreigner_net_purchase_transaction_volume','Foreigner_sold_transaction_price',
        'Foreigner_Purchase_Transaction_Price','Foreigner_Net_Purchase_Transaction_Price','Financial_Investment_Sales_Transaction_Volume','Financial_Investment_Purchase_Transaction_Volume','Financial_Investment_Net_Purchase_Transaction_Volume',
        'Financial_Investment_Sales_Transaction_Price','Financial_Investment_Purchase_Transaction_Price','Financial_Investment_Net_Purchase_Transaction_Price','Investment_Sales_Transaction_Volume','Investment_Purchase_Transaction_Volume',
        'Investment_net_purchase_transaction_volume','Investment_sold_transaction_price','Investment_purchase_transaction_price','Investment_net_purchase_transaction_price','Individual_sold_transaction_volume',
        'Individual_purchase_transaction_volume','individual_net_purchase_transaction_volume','individual_sold_transaction_price','individual_purchase_transaction_price','individual_net_purchase_transaction_price'
    ]
