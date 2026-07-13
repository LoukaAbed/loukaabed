import streamlit as st

st.title('Testing Streamlit and code implementation')
with st.form('batch_files_upload', clear_on_submit=False):
    uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key='dataset')
    upload_button = st.form_submit_button('Upload Dataset')

if st.session_state['dataset']:
    st.write(st.session_state['dataset'][0].name)
    st.session_state['dataset']=[]
    st.rerun()