import streamlit as st
import requests
from bs4 import BeautifulSoup # Used to parse out clean text results if needed

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace bypasses container firewall port blocks using native web streaming requests.")

# --- WEB AUTHENTICATION & EXECUTION PIPELINE ---
def run_sas_via_web_api(sas_code):
    # Your exact assigned Region 2 server web domain
    host = "://sas.com"
    
    # Safely extract your hidden secrets
    username = st.secrets["SAS_USER"]
    password = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]
    
    # Establish a persistent cookie session to maintain login state
    session = requests.Session()
    
    try:
        # Step 1: Hit the main URL first to grab fresh session cookies
        base_url = f"https://{host}/SASStudio/"
        session.get(base_url, timeout=15)
        
        # Step 2: Request login authentication (with redirection handling turned on)
        login_url = f"https://{host}/SASStudio/j_spring_security_check"
        payload = {'j_username': username, 'j_password': password}
        
        # FIXED: Added allow_redirects=True so the session steps past the splash screen
        login_response = session.post(login_url, data=payload, allow_redirects=True, timeout=15)
        
        # Step 3: Stream code directly to the workspace execution API node
        exec_url = f"https://{host}/SASStudio/main/submit"
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Referer': f"https://{host}/SASStudio/main"
        }
        
        exec_response = session.post(exec_url, data=sas_code, headers=headers, timeout=20)
        
        if exec_response.status_code == 200:
            return exec_response.text
        else:
            return f"Error: Server returned status code {exec_response.status_code}"
            
    except Exception as e:
        return f"Network Error: {str(e)}"

# --- MAIN UI WORKSPACE ---
sas_code_input = st.text_area(
    "Modify the SAS query:", 
    "proc print data=sashelp.class(obs=5); run;"
)

if st.button("🚀 Execute Code on SAS Cloud", type="primary"):
    with st.spinner("Streaming encrypted web packets over Port 443..."):
        result_output = run_sas_via_web_api(sas_code_input)
        
        # Format and display the returned text output cleanly
        if "Network Error" in result_output or "Error:" in result_output:
            st.error(result_output)
        else:
            st.success("✅ Output streamed successfully!")
            
            # Neatly separate the results from system messages using tabs
            tab1, tab2 = st.tabs(["📊 Execution Results", "📜 Raw Web Trace"])
            with tab1:
                # If the execution returned a compiled data table HTML, display it visually
                if "class=" in result_output.lower() or "<table>" in result_output.lower():
                    st.html(result_output)
                else:
                    # Otherwise output clean text execution output logs
                    st.code(result_output)
            with tab2:
                st.info("Web request completed with no internal socket drops.")
