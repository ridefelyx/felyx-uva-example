import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("SNOWFLAKE_USER")
password = os.getenv("SNOWFLAKE_PASSWORD")

conn_str = f"snowflake://{user}:{password}@rd02543.europe-west4.gcp/FELYX_UVA/MART?warehouse=COMPUTE_WAREHOUSE_MULTICLUSTER&role=FELYX_UVA"


def query_reservations():
    return pd.read_sql("select * from mrt_reservation limit 10", conn_str)


if __name__ == "__main__":
    print(query_reservations().describe())
