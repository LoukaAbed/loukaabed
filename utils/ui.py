import streamlit as st

def upload(session_state):
    if 'counter' not in st.session_state:
        st.session_state['counter']=0

    with st.form('batch_files_upload', clear_on_submit=True):
        uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key=f"upload_{st.session_state['counter']}")
        upload_button = st.form_submit_button('Upload Dataset')

    if upload_button:
        if uploaded:
            dataset=st.session_state[f"upload_{st.session_state['counter']}"]
            return dataset
            for file in dataset:
                st.write(f"File: {file.name} was successfully uploaded")
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

