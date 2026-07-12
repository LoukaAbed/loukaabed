import streamlit as st
import utils.db as db
import pandas as pd


st.title('Upload Dataset')

st.divider()
schema_name=st.text_input("New DB Schema:", placeholder="db1")
if st.button('Create New Schema'):
    if schema_name.strip:
        st.success(f'You entered: {schema_name}')
