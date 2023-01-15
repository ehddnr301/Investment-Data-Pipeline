CREATE_STOCK_QUERY = """
CREATE TABLE IF NOT EXISTS ods_stock (
날짜 date NOT NULL,
티커 text NOT NULL,
시가 integer NULL,
고가 integer NULL,
저가 integer NULL,
종가 integer NULL,
거래량 bigint NULL,
거래대금 bigint NULL,
등락률 float NULL,
시가총액 bigint NULL,
상장주식수 bigint NULL,
외국인_매도거래량 bigint NULL,
외국인_매수거래량 bigint NULL,
외국인_순매수거래량 bigint NULL,
외국인_매도거래대금 bigint NULL,
외국인_매수거래대금 bigint NULL,
외국인_순매수거래대금 bigint NULL,
금융투자_매도거래량 bigint NULL,
금융투자_매수거래량 bigint NULL,
금융투자_순매수거래량 bigint NULL,
금융투자_매도거래대금 bigint NULL,
금융투자_매수거래대금 bigint NULL,
금융투자_순매수거래대금 bigint NULL,
투신_매도거래량 bigint NULL,
투신_매수거래량 bigint NULL,
투신_순매수거래량 bigint NULL,
투신_매도거래대금 bigint NULL,
투신_매수거래대금 bigint NULL,
투신_순매수거래대금 bigint NULL,
개인_매도거래량 bigint NULL,
개인_매수거래량 bigint NULL,
개인_순매수거래량 bigint NULL,
개인_매도거래대금 bigint NULL,
개인_매수거래대금 bigint NULL,
개인_순매수거래대금 bigint NULL
)
"""

INSERT_STOCK_QUERY = """
INSERT INTO ods_stock
SELECT A.날짜
, A.티커
, A.시가
, A.고가
, A.저가
, A.종가
, A.거래량
, A.거래대금
, A.등락률
, B.시가총액
, B.상장주식수
, C.외국인_매도거래량
, C.외국인_매수거래량
, C.외국인_순매수거래량
, C.외국인_매도거래대금
, C.외국인_매수거래대금
, C.외국인_순매수거래대금
, C.금융투자_매도거래량
, C.금융투자_매수거래량
, C.금융투자_순매수거래량
, C.금융투자_매도거래대금
, C.금융투자_매수거래대금
, C.금융투자_순매수거래대금
, C.투신_매도거래량
, C.투신_매수거래량
, C.투신_순매수거래량
, C.투신_매도거래대금
, C.투신_매수거래대금
, C.투신_순매수거래대금
, C.개인_매도거래량
, C.개인_매수거래량
, C.개인_순매수거래량
, C.개인_매도거래대금
, C.개인_매수거래대금
, C.개인_순매수거래대금
FROM ods_ohlcv AS A
LEFT JOIN ods_marketcap AS B
ON A.티커 = B.티커
LEFT JOIN ods_netpurchase AS C
ON A.티커 = C.티커
"""
