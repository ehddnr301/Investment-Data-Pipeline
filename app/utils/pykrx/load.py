from utils.util import load_data_to_bigquery


def load(df, bigquery_project_id, bigquery_dataset_name, table_name):

    load_data_to_bigquery(df, bigquery_project_id, bigquery_dataset_name, table_name)
