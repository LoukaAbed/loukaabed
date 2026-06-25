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

config_content = f"""
SAS_config_names = ['oda']
oda = {{
    'java': '{JAVA_PATH}',
    'iomhost': '{ODA_SERVER}',
    'iomport': 8591,
    'authkey': 'oda_auth',
    'encoding': 'utf-8'
}}
"""

config_file_path = os.path.abspath("sascfg_personal.py")
with open(config_file_path, "w") as f:
    f.write(config_content)

os.environ["_SAS_SERVER_"] = "odaws01-usw2-2.oda.sas.com"
os.environ["_SAS_USER_"] = st.secrets["SAS_USER"]
os.environ["_SAS_PASS_"] = st.secrets["SAS_PASSWORD"]

@st.cache_resource  # <-- 1. Guard: Checks memory. If connection exists, skips the code below.
def get_sas_session():
    try:
        # <-- 2. Worker: Only runs ONCE to build the initial cloud tunnel.
        sas = saspy.SASsession(cfgfile=config_file_path, cfgname="oda")
        return sas
    except Exception as e:
        return None

def get_sas_session():
    try:
        sas = saspy.SASsession(cfgfile=config_file_path, cfgname="oda")
        return sas
    except Exception as e:
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

# Group pages and initialize navigation (Updated to include your target pages)
nav = st.navigation([home_page, third_page, fourth_page])
nav.run()
