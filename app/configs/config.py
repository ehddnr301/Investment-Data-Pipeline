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
