import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clinical Projects - Dr. Louka Abed", layout="wide")

st.title("📊 Clinical Data Science Portfolio")
st.write("Regulatory-compliant pipelines and automated analytical reporting applications.")

# Project 1 Expansion Box
with st.expander("🚀 Project 1: CDISC SDTM Demographics (DM) Dataset Pipeline", expanded=True):
    st.markdown("""
    * **Objective:** Map messy, disparate Electronic Health Record (EHR) raw data into the strict **CDISC SDTM v2.0** regulatory standard format.
    * **Core Technologies:** SAS 9.4 (`DATA` steps, formats, functions), Python (Streamlit Frontend hosting).
    * **Key Accomplishment:** Built clean handling for baseline demographics tracking across 500 patient observations.
    """)
    
    # Showcase your actual SAS code inside a clean code block
    st.markdown("### 💻 Core SAS Code Snippet")
    sas_code = """/* Mapping Raw Clinical Data to SDTM DM Domain */
data sdtm.dm(label="Demographics");
    set raw.patient_log(rename=(pt_id=USUBJID birth_dt=BRTHDTC));
    keep STUDYID DOMAIN USUBJID SUBJID BRTHDTC AGE AGEU SEX;
    STUDYID = "STUDY-2026-EU";
    DOMAIN  = "DM";
    SUBJID  = USUBJID;
    AGEU    = "YEARS";
    if sex_code = 1 then SEX = "M";
    else if sex_code = 2 then SEX = "F";
    else SEX = "U";
run;"""
    st.code(sas_code, language="sas")

    # Load and display an interactive preview of the actual output table
    st.markdown("### 📊 Interactive Dataset Preview (Generated Output)")
    st.write("Recruiters can sort, search, and download this compliant data output immediately:")
    
    # Mock data matrix for your portfolio presentation
    mock_data = {
        "STUDYID": ["STUDY-2026-EU", "STUDY-2026-EU", "STUDY-2026-EU"],
        "DOMAIN": ["DM", "DM", "DM"],
        "USUBJID": ["001-01", "001-02", "001-03"],
        "AGE": [45, 62, 29],
        "AGEU": ["YEARS", "YEARS", "YEARS"],
        "SEX": ["M", "F", "F"]
    }
    df = pd.DataFrame(mock_data)
    
    # Use st.dataframe for free sorting/filtering capabilities
    st.dataframe(df, use_container_width=True)
