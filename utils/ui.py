import streamlit as st
import utils.db as db
import os
from sqlalchemy import create_engine, inspect, MetaData, text
bridge = create_engine(os.environ.get("NEON_DB_URL"), echo=True, pool_pre_ping=True, pool_recycle=300 )


def upload():
    if 'dataset_dic' not in st.session_state:
        st.session_state['dataset_dic']={}
    col1, col2 = st.columns(2)
    with col1:
        with st.form('batch_files_upload', clear_on_submit=True):
            uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key='upload')
            upload_button = st.form_submit_button('Submit For Dataset Upload')
        with col2:
            selected_schema = st.selectbox("Select target schema for upload", inspect(bridge).get_schema_names())

    if upload_button:
        if uploaded and len(uploaded)>0:
            with st.spinner(f"Uploading files into 'public' schema. Processing..."):
                dataset=st.session_state['upload']
                dataset_dic={}
                for file in st.session_state['dataset_dic']:
                    file_key = db.name_db(file.name, prefix='', name_type='file')
                    dataset_dic[file_key] = file
                st.session_state['dataset_dic'] = db.dataset_db(dataset, schema=selected_schema, prefix='', if_exists='replace')
        else:
            st.warning('Please upload the files before clicking submit')






def maxfile_size(max_size=2):
    """Change the displayed default size setting on the upload button to a custom argument max_size"""
    st.markdown(

        f"""
        <style>
        /* 1. correct container wrapper to remove 200MB label */
        div[data-testid="stFileUploaderDropzoneInstructions"] > div > small {{
        display: none !important;
        }}
    
        /* 2. correct fallback label wrappers if present */
        div[data-testid="stFileUploaderDropzoneInstructions"] > div > span {{
        display: none !important;
        }}
    
        /* 3. Showing Accurate File Uploader total Size */
        div[data-testid="stFileUploaderDropzoneInstructions"] > div::after {{
        content: "Limit Max Upload Size {max_size}MB";
        display: block;
        font-size: 0.8rem;
        color: #666666;
        margin-top: 4px;
        }}
        </style>
        """,
        unsafe_allow_html=True,)

