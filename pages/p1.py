import os
import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd
import uuid

#this page made to test the connection to the database
st.title("📈 Database Connection Test")

st.divider()

#first let's establish connection
#getting the database url
url=os.environ.get("NEON_DB_URL")

#establishing bridge to the database
bridge=create_engine(url)


#let's user upload a csv small 2MB or less file to be stored in the database
uploaded_csv = st.file_uploader("Upload csv <= 2MB to be stored in the database", type=["csv"])




def safe(file_1):
    if uploaded_csv is not None:
        if "File1Name" not in st.session_state:
            hex_name = uuid.uuid4().hex
            st.session_state["File1Name"]=f"user_{hex_name}"
            st.write(hex_name)
            st.write(st.session_state)


safe(uploaded_csv)

#Let's check the uploaded file for size and security check and prevent malicious code injection into the database.
if uploaded_csv is not None and not st.session_state.get('upload_deleted', False):
    st.session_state['file_uploaded']=True
    #remove space from name of the file, and storing the full file name with extension and without in two variables
    file_name = uploaded_csv.name.split('.')[0].replace(' ', '_')
    file_nameCSV = file_name + '.csv'
    file1name=st.session_state["File1Name"]

    if uploaded_csv.size > 2*1024*1024:
        st.error(f"[Upload Error] : {file_nameCSV} size exceeded 2MB limit. Please upload a smaller file.")
        st.stop() #stop the execution
    df = pd.read_csv(uploaded_csv)
    df.columns= df.columns.str.strip().str.lower().str.replace(' ', '_') #remove spaces and convert to lower case for column names

    #upload file to the database, replace if exists
    df.to_sql(name=file1name, con=bridge, if_exists='replace', index=False)
    st.session_state['upload_success']=True
    st.write(f"your {file_nameCSV} file was uploaded successfully to the database")
    #Returning the first five rows of the uploaded
    st.write(f"First five rows of the uploaded {file_nameCSV}")
    sql_query=f"SELECT * FROM {file1name} LIMIT 5"
    result = pd.read_sql(sql_query, con=bridge)
    st.write(result)
if 'File1Name' in st.session_state:
    file1name=st.session_state["File1Name"]
    file_name = uploaded_csv.name.split('.')[0].replace(' ', '_')
    file_nameCSV = file_name + '.csv'
    if st.button(f"Delete  {file_nameCSV} Completely from the database"):
        with bridge.begin() as connection:
            sql_query = f"DROP TABLE IF EXISTS {file1name}"
            connection.execute(text(sql_query))
            del st.session_state["File1Name"]
            st.session_state['upload_deleted']=True
            st.rerun() 
if 'File1Name' not in st.session_state: 
    if st.session_state.get('upload_deleted', False):
        st.success(f"{file_nameCSV} has been completely deleted from the database.")