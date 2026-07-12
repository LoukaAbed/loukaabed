import pandas as pd
import os
import uuid
from sqlalchemy import create_engine, text
from typing import Literal
import re

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

def name_db(prefix='user_', tbl_name='uuid'):
    tbl=''
    if tbl_name != 'uuid':
        if '.' in tbl_name:
            file_name, extension = tbl_name.rsplit('.', 1)
            extension = extension.lower()
            tbl= f"{prefix}{re.sub(r'[_]+', '_', re.sub(r'[^a-zA-Z0-9_]', '_', file_name)).lower()}_{extension}"
        else:
            file_name=tbl_name
            extension=''
            tbl= f"{prefix}{re.sub(r'[_]+', '_', re.sub(r'[^a-zA-Z0-9_]', '_', file_name)).lower()}"
    else:
        tbl= prefix + uuid.uuid4().hex
    if tbl[0].isdigit() or tbl[0]=='_':
        return f'x_{tbl}'
    else:
        return tbl


def store_db(uploaded_file, prefix='', tbl_name='uuid', if_tbl_exist: Literal['append', 'replace', 'fail']='replace', destination_schema='public'):
    df = pd.read_csv(uploaded_file)
    safe_tbl_name = name_db(prefix, tbl_name)
    with bridge.begin() as conn:
        df.to_sql(safe_tbl_name, con=conn, schema=destination_schema, if_exists=if_tbl_exist, index=False)
    return safe_tbl_name

def drop_db(tbl_name):
    with bridge.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {tbl_name}"))
