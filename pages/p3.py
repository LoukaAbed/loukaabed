import streamlit as st

st.title('Testing Streamlit and code implementation')


if 'counter' not in st.session_state:
    st.session_state['counter']=0
with st.form('batch_files_upload', clear_on_submit=False):
    uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key=f"{st.session_state['counter']}")
    upload_button = st.form_submit_button('Upload Dataset')

if upload_button:
    if not uploaded:
        st.warning('Please add files to upload first before clicking upload')
    else:
        dataset = st.session_state[f"{st.session_state['counter']}"]
        st.success(st.session_state[f"Your file: {st.session_state['counter']} was successfuly uploaded"][0].name)
        for file in dataset:
            st.success(f"Your file: {file.name} was successfuly uploaded")
        st.session_state['counter'] +=1
        st.rerun()