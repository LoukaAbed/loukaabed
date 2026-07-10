import os
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

#this page made to test the connection to the database
st.title("📈 Database Connection Test")

st.divider()

#first let's establish connection
#getting the database url
url=os.environ.get("NEON_DB_URL")

#establishing bridge to the database
bridge=create_engine(url)

#let's user upload a csv small 2MB or less file to be stored in the database
uploaded_csv = st.file_uploader("Upload csv <2MB to be stored in the database", type=["csv"])

#Let's check the uploaded file for size and security check to prevent malicious code injection into the database.
if uploaded_csv is not None :
    if uploaded_csv.size > 2*1024*1024:
        st.error(f"[Upload Error] : {uploaded_csv.name} size exceeded 2MB limit. Please upload a smaller file.")
        st.stop() #stop the execution
    df = pd.read_csv(uploaded_csv)
    cleaned_df= df.columns.str.strip().str.lower().str.replace(' ', '_')

    #upload file to the database, replace if exists
    cleaned_df.to_sql(uploaded_csv.name.split('.')[0], con=bridge, if_exists='replace', index=False)
    st.write(f"your {uploaded_csv.name.split('.')[0]} file was uploaded successfully to the database")

    #Returning the first five rows of the uploaded
    st.write(f"First five rows of the uploaded {uploaded_csv.name}")
    sql_query=f"SELECT * FROM {uploaded_csv.name.split('.')[0]} LIMIT 5"
    result = pd.read_sql(sql_query, con=bridge)
    st.write(result)