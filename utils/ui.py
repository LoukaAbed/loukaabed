import streamlit as st
import utils.db as db
import os
import base64
import mimetypes
import requests  
from sqlalchemy import create_engine, inspect, MetaData, text

bridge=db.bridge_db()

    
def upload():
    if 'dataset_dic' not in st.session_state:
        st.session_state['dataset_dic']={}
    col1, col2 = st.columns(2)
    with col1:
        with st.form('batch_files_upload', clear_on_submit=True):
            uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key='upload')
            upload_button = st.form_submit_button('Submit Dataset For Upload')
        with col2:
            selected_schema = st.selectbox("Select Target Schema To Upload Dataset To", inspect(bridge).get_schema_names())

    if upload_button:
        if uploaded and len(uploaded)>0:
            with st.spinner(f"Uploading files into 'public' schema. Processing..."):
                dataset=st.session_state['upload']
                dataset_dic={}
                for file in st.session_state['dataset_dic']:
                    file_key = db.name_db(file, prefix='', name_type='file')
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

def send(name, email, subject, body, attached_files=None):
    try:
        google_script = os.environ.get("GOOGLE_SCRIPT_URL")
        if not google_script:
            return False, "System Configuration Error"
        message_data = {"name": name, "email": email, "subject": subject, "message": body, "attachments": attached_files if attached_files else []}

        # Expanded timeout to 30 seconds to accommodate large file(s) attachment
        network_response = requests.post(google_script, json=message_data, allow_redirects=True, timeout=30)
        if network_response.status_code == 200:
            return (True, "Success")
        else:
            return (False, f"Server responded with an error: {network_response.status_code}")

    except Exception as network_exception:
        return (False, f"Network failure: {network_exception}")


def message():
    maxfile_size(max_size=25)
    # Message Form
    st.markdown("### Professional Inquiries")
    st.markdown("Please use the form below for recruitment inquiries or project collaborations. You may also contact me directly at [contact@loukaabed.com](mailto:contact@loukaabed.com?subject=Professional%20Inquiry)")
    with st.form("contact_form", clear_on_submit=True):
        left, right = st.columns(2)
        with left:
            name = st.text_input("Your name or company", placeholder="John Doe or Company Name")
            subject = st.text_input("Subject", placeholder="e.g., Recruitment / Collaboration")
        with right:
            email = st.text_input("Return Email Address", placeholder="name@organization.com")
        message_body = st.text_area("Message", placeholder="Please type your message here...")
        uploaded_files = st.file_uploader("Upload Attachments With Max Total Size: 25MB", accept_multiple_files=True)
        submit = st.form_submit_button("✉️ Send Message")
        if submit:
            if not name or not email or not message_body:
                st.warning("Please complete all fields before sending your message")
            elif "@" not in email or "." not in email:
                st.error("Please provide a valid return email.")
            else:                
                attached_files = []
                size = 0
                if uploaded_files:
                    for file in uploaded_files:
                        size += file.size
                        if size > 25 * 1024 * 1024:
                            st.error("Total combined file sizes exceeded 25MB attachment limit.")
                            st.stop()
                        file_data = file.read()
                        file.seek(0)
                        attached_files.append({
                            "bytes": base64.b64encode(file_data).decode("utf-8"), 
                            "filename": file.name, 
                            "mime_type": (mimetypes.guess_type(file.name) or ("application/octet-stream",))[0]})

                sent, log = send(name, email, subject, message_body, attached_files)
                if sent:
                    st.success("Your message was sent successfully to contact@loukaabed.com. Thank you.")
                else:
                    st.error(log)