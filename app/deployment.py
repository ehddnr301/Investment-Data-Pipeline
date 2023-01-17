from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import CronSchedule

from main import stock_data_etl

stock_etl = Deployment.build_from_flow(
    flow=stock_data_etl,
    name="stock_etl",
    work_queue_name="wq_stock_etl",
    schedule=(CronSchedule(cron="0 18 * * *", timezone="Asia/Seoul")),
)

if __name__ == "__main__":
    stock_etl.apply()
