import streamlit as st
import utils.db as db
import pandas as pd


st.title('Upload Dataset')

st.divider()
schema_name=st.text_input("New DB Schema:", placeholder="db1")
if st.button('Create New Schema'):
    if schema_name.strip:
        safe_name=name_db(schema_name, prefix='', name_type='file'):
        st.success(f'Schema name after format: {safe_name}')
