import streamlit as st

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
