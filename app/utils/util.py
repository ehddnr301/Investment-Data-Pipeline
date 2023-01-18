import psycopg2
import pandas as pd
import psycopg2.extras as extras
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from configs.config import Config


def initial_load_data(engine: Engine, df: pd.DataFrame, table_name: str):
    with engine.begin() as conn:
        df.to_sql(table_name, con=conn, index=False)


def load_data(conn, df, table_name):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ",".join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" % (table_name, cols)
    cursor = conn.cursor()

    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        cursor.close()
        print(error)
    cursor.close()


def create_db_connection(engine_type: str):
    if engine_type == "psycopg":
        return psycopg2.connect(
            host=Config.POSTGRES_HOST,
            database=Config.POSTGRES_DATABASE,
            port=Config.POSTGRES_PORT,
            user=Config.POSTGRES_USER,
            password=Config.POSTGRES_PASSWORD,
        )
    if engine_type == "sqlalchemy":
        return create_engine(
            "postgresql://{}:{}@{}:{}/{}".format(
                Config.POSTGRES_USER,
                Config.POSTGRES_PASSWORD,
                Config.POSTGRES_HOST,
                Config.POSTGRES_PORT,
                Config.POSTGRES_DATABASE,
            )
        )


def check_table_exists(engine: Engine, table_name: str):
    is_exists = engine.has_table(table_name)

    return is_exists
