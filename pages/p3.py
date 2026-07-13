import streamlit as st

st.title('Testing Streamlit and code implementation')


if 'counter' not in st.session_state:
    st.session_state['counter']=0
with st.form('batch_files_upload', clear_on_submit=False):
    uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key=f"{st.session_state['counter']}")
    upload_button = st.form_submit_button('Upload Dataset')

if st.session_state[f"{st.session_state['counter']}"]:
    st.write(st.session_state[f"{st.session_state['counter']}"][0].name)
    st.session_state['counter'] +=1
    st.rerun()