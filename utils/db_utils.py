import pandas as pd
import os
import uuid
from sqlalchemy import create_engine, text

#build connection to the database
bridge = create_engine(os.environ.get("NEON_DB_URL"), echo=True)

def fetch_db(query, query_dic=None):
    with bridge.connect() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())

def edit_db(query, query_dic=None):
    with bridge.begin() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())   

def name_db():
    return 'user_' + uuid.uuid4().hex

def store_db(uploaded_file):
    df = pd.read_csv(uploaded_file)
    tbl_name = name_db()
    with bridge.begin() as conn:
        df.to_sql(tbl_name, con=conn, if_exists='replace', index=False)
    return tbl_name