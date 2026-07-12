import streamlit as st
import utils.db as db
import pandas as pd


st.title('Upload Dataset')

st.divider()
schema_name=st.text_input("New DB Schema:", placeholder="db1")
if st.button('Create New Schema'):
    if schema_name.strip():
        safe_name=db.name_db(tbl_name=schema_name, prefix='', name_type='file')
        st.success(f'New schema name was created as: {db.schema_db(schma=safe_name, need='new_schema')}')
    else:
        st.warning("The input field is empty. Please enter text.")