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

""""
with st.form(key='delete_selector', border=False):
    col1, col2 = st.columns([1, 2], vertical_alignment="center")
    with col1:
        bttn = st.form_submit_button("Delete Schema")
    with col2:
        selector=st.selectbox("Choose schema to delete", db.inside_db(need='schema'))

if bttn and selector: 
    st.success(f"Schema: {db.schema_db(schma=selector, need='delete_schema')} was successfuly deleted")
    st.rerun()
"""
dataset = st.file_uploader("Upload multiple files dataset:", type=None, accept_multiple_files=True, key="dataset_upload")
if dataset: 
    if st.button('Upload Dataset'):
        with st.spinner(f"Uploading files into 'mimic4demo' schema. Processing..."):
            tables=db.dataset_db(dataset, schema='mimic4demo')
            if tables:
                st.success(f"Originally {len(dataset)} files detected and successfully processed and stored {len(tables)} tables!")

                for tbl_name, table in tables.items():
                    st.code(f"Database Table Created: {tbl_name} ({len(table)} rows)")
            else:
                st.warning("Files with no supported extensions (.csv, .xlsx, .tsv, .txt, .dat).")
