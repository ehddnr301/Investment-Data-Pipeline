# Pykrx-Data-Pipeline

## Project Environment

- GCP Compute Engine (e2-medium vCPU2, 4GB memory, Ubuntu 20.04.5 LTS)
- Docker version 20.10.22
- docker-compose version 1.25.0
- pre-commit: black

## To-Do List (2023-01-15)

- [ ] 각 데이터 Table로 Insert후 하나의 테이블로 합치는 형태
- [ ] Insert Performance 향상
- [ ] 중복데이터 처리 로직 추가
- [ ] Prefect 로 스케줄 관리
- [ ] Notification 추가
- [ ] Postgres를 대체할 DB형태 고려

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
