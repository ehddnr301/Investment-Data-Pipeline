from datetime import datetime, timedelta

from configs.config import Config
from utils import extract_pykrx, transform_pykrx, load_pykrx
import logging
import traceback


def try_catch_log(wrapped_func):
    def wrapper(*args, **kwargs):
        try:
            response = wrapped_func(*args, **kwargs)
        except Exception:
            error_message = traceback.format_exc().replace("\n", "  ")
            logging.error(error_message)
            return "Error"
        return response

    return wrapper


@try_catch_log
def stock_data_etl2(request=None):
    basedate = request.get_json().get("basedate") or str(
        (datetime.today() + timedelta(hours=9)).date()
    )

    ohlcv_df, marketcap_df, netpurchase_df = extract_pykrx(
        basedate,
        Config.TARGET_NAME_LIST,
        Config.DROP_COLUMN_LIST,
        Config.INVESTOR_LIST,
    )
    df = transform_pykrx(ohlcv_df, marketcap_df, netpurchase_df)
    print(df.shape)
    load_pykrx(df, Config.BIGQUEY_PROJECT_ID, Config.BIGQUEY_DATASET_NAME, "t_stock")

    return "Done"
