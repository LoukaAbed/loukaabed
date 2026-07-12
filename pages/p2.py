import streamlit as st
import utils.db as db
import pandas as pd


st.title('Upload Dataset')

st.divider()
schema_name=st.text_input("New DB Schema:", placeholder="db1")
if st.button('Create New Schema'):
    if schema_name.strip():
        safe_name=db.name_db(tbl_name=schema_name, prefix='', name_type='file')
        st.success(f'New schema name was created as: {db.schema_db(schma=safe_name, need='delete_schema')}')
    else:
        st.warning("The input field is empty. Please enter text.")

col1, col2 = st.columns([1, 1])
with col1:
    bttn = st.button('Delete Schema')
with col2:
    selector= selected_option = st.selectbox("Choose schema to delete :", db.inside_db(need='schema'))

if bttn and selector:
    st.success(f'Schema: {db.schema_db(schma=safe_name, need='delete_schema')} was successfuly deleted')
else:
    st.warning("Choose schema to delete and click delete")