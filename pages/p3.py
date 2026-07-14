import streamlit as st
import utils.ui as ui

st.title('Testing Streamlit and code implementation')


# if 'counter' not in st.session_state:
#     st.session_state['counter']=0
# with st.form('batch_files_upload', clear_on_submit=True):
#     uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key=f"upload_{st.session_state['counter']}")
#     upload_button = st.form_submit_button('Upload Dataset')

# if upload_button:
#         if uploaded:
#             dataset=st.session_state[f"upload_{st.session_state['counter']}"]
#             for file in dataset:
#                 st.write(f"File: {file.name} was successfully uploaded")
#         else:
#             st.warning('Please upload the files before clicking submit')


dataset = ui.upload()
files=[]
if dataset is not None:
    for file in dataset:
        files.append(file.name)
    st.write(files)
