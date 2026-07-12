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


with st.form(key='delete_selector', border=False):
    col1, col2 = st.columns([1, 2], vertical_alignment="center")
    with col1:
        bttn = st.form_submit_button("Delete Schema")
    with col2:
        selector=st.selectbox("Choose schema to delete", db.inside_db(need='schema'))

if bttn and selector: 
    st.success(f"Schema: {db.schema_db(schma=selector, need='delete_schema')} was successfuly deleted")
    st.rerun()

uploaded_file = st.file_uploader("Upload a CSV file: Max Size 2MB", type=["csv"], key=uploader_key)

