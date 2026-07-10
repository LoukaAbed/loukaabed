import streamlit as st
import os
from sqlalchemy import create_engine, text

st.title("Neon Database Connection Test")
st.divider()

#build connection to the database
bridge = create_engine(os.environ.get("NEON_DB_URL"), echo=True)

def db_fetch(query, var_dic=None):
    with bridge.connect() as conn:
        result = conn.execute(text(query), var_dic)
        return result.fetchall()
    
query = "SELECT * FROM bp where gender = :gender and age > :age"
st.write(db_fetch(query, {"gender": "Male", "age": 25}))
