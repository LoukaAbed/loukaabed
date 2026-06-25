import os
import streamlit as st
import saspy

st.set_page_config(page_title="My App")

# Define your pages
home_page = st.Page("hello.py", title="Home", icon="🏠")
another_page = st.Page("analytics.py", title="test", icon="📊")
third_page = st.Page("hellostreamlit.py", title="test", icon="👋")
fourth_page = st.Page('sas.py', title='SAS Experience', icon='👋')

# --- BACKEND SAS CONFIGURATION ENGINE ---
JAVA_PATH = "/usr/bin/java"
ODA_SERVER = "odaws01-usw2-2.oda.sas.com"

# Safely extract secrets first
sas_user_credential = st.secrets["SAS_USER"]

if "SAS_PASSWORD" in st.secrets:
    sas_pass_credential = st.secrets["SAS_PASSWORD"]
else:
    sas_pass_credential = st.secrets["SAS_PASS"]

# FIX: Injected 'user' and 'pw' explicitly into the connection definition dictionary.
# Dropped 'authkey' entirely to prevent the Java sub-process from triggering a prompt loop.
config_content = f"""
SAS_config_names = ['oda']
oda = {{
    'java': '{JAVA_PATH}',
    'iomhost': '{ODA_SERVER}',
    'url': 'https://{ODA_SERVER}:443',
    'user': '{sas_user_credential}',
    'pw': '{sas_pass_credential}',
    'encoding': 'utf-8',
    'omr': False
}}
"""

config_file_path = os.path.abspath("sascfg_personal.py")
with open(config_file_path, "w") as f:
    f.write(config_content)

# Also expose variables to the broader environment layer for fallback redundancy
os.environ["_SAS_SERVER_"] = ODA_SERVER
os.environ["_SAS_USER_"] = sas_user_credential
os.environ["_SAS_PASS_"] = sas_pass_credential

@st.cache_resource
def get_sas_session():
    try:
        # Establish connection using explicit parameters
        sas = saspy.SASsession(cfgfile=config_file_path, cfgname="oda")
        return sas
    except Exception as e:
        # Catch and display exact error trace inside the app sidebar for easy debugging
        st.sidebar.error(f"Internal SASPy Connection Error: {e}")
        return None

# Attempt backend connection and cache it globally
sas_session = get_sas_session()

# --- LANDING PAGE CONTENT & INTERFACE ---
st.title("Welcome to the Portfolio Hub")

if sas_session:
    # Save session state globally so sub-pages can inherit the open connection line
    st.session_state["sas_conn"] = sas_session
    st.success("✅ Backend engine successfully linked to SAS OnDemand for Academics.")
    
    # Navigation link directly targeting the fourth page (SAS Experience)
    st.markdown("---")
    st.subheader("Explore the Cloud Analytical Environment")
    if st.button("👉 View Active SAS Workspace"):
        st.switch_page(fourth_page)
else:
    st.error("❌ Failed to initiate underlying SAS cloud connection. Check Hugging Face Secrets setup logs.")
    st.info("💡 Look closely at your application's left sidebar to inspect the direct error code output from SASPy.")

# Group pages and initialize navigation 
nav = st.navigation([home_page, third_page, fourth_page])
nav.run()
