import pandas as pd
import os
import uuid
from sqlalchemy import create_engine, text
from typing import Literal

#build connection to the database options pool_pre_ping, pool_recycle prevent db crash on startup  
bridge = create_engine(os.environ.get("NEON_DB_URL"), echo=True, pool_pre_ping=True, pool_recycle=300 )

def fetch_db(query, query_dic=None):
    with bridge.connect() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())

def edit_db(query, query_dic=None):
    with bridge.begin() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())   

def name_db(prefix):
    return prefix + uuid.uuid4().hex

def store_db(uploaded_file, prefix='user_', if_tbl_exist: Literal['append', 'replace', 'fail']='replace', destination_schema='public'):
    df = pd.read_csv(uploaded_file)
    tbl_name = name_db(prefix)
    with bridge.begin() as conn:
        df.to_sql(tbl_name, con=conn, schema=destination_schema, if_exists=if_tbl_exist, index=False)
    return tbl_name

def drop_db(tbl_name):
    with bridge.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {tbl_name}"))
