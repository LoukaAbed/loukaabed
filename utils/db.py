import pandas as pd
import os
import uuid
from sqlalchemy import create_engine, inspect, MetaData, text
from sqlalchemy.schema import CreateSchema, DropSchema
from typing import Literal
import re
import streamlit as st

@st.cache_resource
def bridge_db():
    return create_engine(os.environ.get("NEON_DB_URL"), echo=True, pool_pre_ping=True, pool_recycle=300 )

#build connection to the database options pool_pre_ping, pool_recycle prevent db crash on startup  
bridge = bridge_db()

def fetch_db(query, query_dic=None):
    with bridge.connect() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())

def edit_db(query, query_dic=None):
    with bridge.begin() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())   


def name_db(tbl_name, prefix='user_', name_type='uuid'):
    tbl=''
    if name_type == 'file':
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


def store_db(uploaded_file, prefix='user_', name_type: Literal['file', 'uuid']='file', if_tbl_exist: Literal['append', 'replace', 'fail']='replace', destination_schema='public'):
    df = pd.read_csv(uploaded_file)
    file= uploaded_file.name
    safe_tbl_name = name_db(file, prefix, name_type)
    with bridge.begin() as conn:
        df.to_sql(safe_tbl_name, con=conn, schema=destination_schema, if_exists=if_tbl_exist, index=False)
    return safe_tbl_name

def drop_db(tbl_name):
    with bridge.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {tbl_name}"))

def schema_db(schma='db1', need: Literal['new_schema', 'delete_schema', 'empty_schema']='new_schema'):
    all_schemas = inspect(bridge).get_schema_names()
    with bridge.begin() as conn:
        if schma in all_schemas and need=='delete_schema':
            conn.execute(DropSchema(schma, if_exists=True, cascade=True))
            return schma
        elif schma in all_schemas and need=='empty_schema':
            x=MetaData(schema=schma) 
            x.reflect(bind=bridge)
            x.drop_all(conn)
            return schma
        elif need=='new_schema':
            conn.execute(CreateSchema(schma, if_not_exists=True))
            return schma
    return False
def inside_db(need='schema'):
    return inspect(bridge).get_schema_names()

def dataset_db(dataset, schema='public', prefix='', if_exists='replace'):
    dataset_dic = {}
    with bridge.begin() as conn:
        for file in dataset:
            if hasattr(file, 'seek'):
                file.seek(0)
            df=''
            file_key = name_db(file.name, prefix, name_type='file')
            if file.name.endswith(('.tsv', '.txt', '.dat')):
                df = pd.read_csv(file, sep=None, engine='python')
            elif file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            if isinstance(df, str):
                continue
            df.to_sql(name=file_key, con=conn, schema=schema, if_exists=if_exists, index=False)
            dataset_dic[file_key] = df
    return dataset_dic


