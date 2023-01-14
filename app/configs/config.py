import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

class Config:
    POSTGRES_URL:str = os.getenv("POSTGRES_URL")
    TARGET_NAME_LIST:List[str] =  [
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
    INVESTOR_LIST:List[str] = ["외국인", "금융투자", "투신", "개인"]