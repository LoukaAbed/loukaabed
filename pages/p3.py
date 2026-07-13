import streamlit as st

if 'dataset' not in st.session_state: 
    st.session_state['dataset']=None

with st.form('batch_files_upload', clear_on_submit=False):
    uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key='dataset')
    upload_button = st.form_submit_button('Upload Dataset')
st.write(st.session_state['dataset'])