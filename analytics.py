import os
import streamlit as st
import saspy

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace connects to the ODA servers independently.")

# --- BACKGROUND SYSTEM WORKER ---
def build_sas_profile_and_connect():
    JAVA_PATH = "/usr/bin/java"
    ODA_SERVER = "://sas.com" # Region 2 server

    # Safely extract your hidden secrets
    sas_user = st.secrets["SAS_USER"]
    sas_pass = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]

    # Generate a headless profile file directly in the container home directory
    home_directory = os.path.expanduser("~")
    authinfo_path = os.path.join(home_directory, ".authinfo")
    with open(authinfo_path, "w") as f:
        f.write(f"oda user {sas_user} password {sas_pass}\n")
    os.chmod(authinfo_path, 0o600)

    # Re-apply the stable Java connection mapping block
    config_content = f"""
SAS_config_names = ['oda']
oda = {{
    'java': '{JAVA_PATH}',
    'iomhost': '{ODA_SERVER}',
    'iomport': 8591,
    'authkey': 'oda',
    'encoding': 'utf-8'
}}
"""
    config_file_path = os.path.abspath("sascfg_personal.py")
    with open(config_file_path, "w") as f:
        f.write(config_content)
        
    return config_file_path

# --- CACHE ENGINE WITH RAW DIAGNOSTICS ---
@st.cache_resource(show_spinner="Connecting to SAS Cloud Engine...")
def load_subpage_sas_session():
    try:
        cfg_path = initialize_sas_profile_path = build_sas_profile_and_connect()
        
        # Instantiate SAS session manually to extract hidden driver logs if it crashes
        sas = saspy.SASsession(cfgfile=cfg_path, cfgname="oda")
        return sas
    except Exception as e:
        st.error(f"❌ Internal System Error: {e}")
        
        # DIAGNOSTIC DUMP: Look into the SASPy internal object log tracker
        try:
            import sys
            # Attempt to pull the raw system execution log from the underlying object
            st.subheader("📋 Underlying System Diagnostic Log:")
            if 'sas' in locals() and hasattr(sas, 'logger'):
                st.code(sas.logger, language="text")
            else:
                st.info("No lower-level Java logs were generated before the process was killed.")
        except:
            pass
        return None

# Trigger connection exclusively inside this view state
sas_session = load_subpage_sas_session()

if sas_session:
    st.success("✅ Securely connected to SAS OnDemand for Academics.")
    sas_code = "proc print data=sashelp.class(obs=5); run;"
    res = sas_session.submit(sas_code)
    st.html(res['LST'])
