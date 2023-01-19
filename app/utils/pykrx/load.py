from prefect import task

from utils.util import load_data_to_bigquery


@task(name="KrxStock_Load")
def load(df, bigquery_project_id, bigquery_dataset_name, table_name):

    load_data_to_bigquery(df, bigquery_project_id, bigquery_dataset_name, table_name)
