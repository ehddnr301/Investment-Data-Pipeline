# Pykrx-Data-Pipeline

## Project Environment

- GCP Compute Engine (e2-medium vCPU2, 4GB memory, Ubuntu 20.04.5 LTS)
- Docker version 20.10.22
- docker-compose version 1.25.0
- pre-commit: black


## To-Do List (2023-01-19)

- [ ] Postgres를 대체할 DB형태 고려
## To-Do List (2023-01-18)

- [x] Notification 추가

## To-Do List (2023-01-17)

- [x] Prefect 로 스케줄 관리

## To-Do List (2023-01-15)

- [x] 중복데이터 처리 로직 추가
- [x] Insert Performance 향상

## To-Do List (2023-01-13)

- [x] pykrx 테스트
    - [x] ohlcv
    - [x] marketcap
    - [x] 외국인(foreigner)
    - [x] 금융투자(brokerage)
    - [x] 투신(investment)
    - [x] 개인(individual)
- [x] db 저장 (postgres)
- [x] Dockerfile형태 제작
- [x] docker-compose형태 제작
- [x] crontab 설정
