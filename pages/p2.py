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
    st.success(f"Schema: {db.schema_db(schma=selector, need='empty_schema')} was successfuly deleted")
    st.rerun()

if 'uploaded' not in st.session_state:
    st.session_state['uploaded']=None

dataset = st.file_uploader("Upload multiple files dataset:", type=None, accept_multiple_files=True, key="dataset_upload")
if dataset: 
    if st.button('Upload Dataset'):
        with st.spinner(f"Uploading files into 'public' schema. Processing..."):
            tbl_dic=db.dataset_db(dataset, schema='mimic4demo')
            st.session_state['uploaded']=tbl_dic
    if st.session_state['uploaded'] is not None:
        saved_tbl_dic = st.session_state['uploaded']
        if saved_tbl_dic:
            st.success(f"Originally {len(dataset)} files detected, successfully processed and stored {len(saved_tbl_dic)} tables!")

            for tbl_name, table in saved_tbl_dic.items():
                st.code(f"Database Table Created: {tbl_name} ({len(table)} rows)")
        else:
            st.warning("Files with no supported extensions, only (.csv, .xlsx, .tsv, .txt, .dat) accepted.")
