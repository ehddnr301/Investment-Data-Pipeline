from prefect import task

from utils.util import (
    create_db_connection,
    check_table_exists,
    load_data,
    initial_load_data,
)


@task(name="KrxStock_Load")
def load(df, table_name):
    # Create Connection
    psycopg_conn = create_db_connection("psycopg")
    sqlalchemy_engine = create_db_connection("sqlalchemy")

    # Check Table Exists
    is_exists = check_table_exists(sqlalchemy_engine, table_name)

    # Load Data
    if is_exists:
        load_data(psycopg_conn, df, table_name)
    else:
        initial_load_data(sqlalchemy_engine, df, table_name)
