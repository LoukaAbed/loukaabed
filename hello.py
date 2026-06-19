import streamlit as st
import requests  # Handles the clean web traffic to Google
import os

# Set page configuration at the absolute top to prevent rendering crashes
st.set_page_config(
    page_title="Dr. Louka Abed | Clinical Data Science Gateway",
    layout="wide",
    initial_sidebar_state="expanded"
)
def transmit_pharma_lead(recruiter_name, recruiter_email, lead_subject, lead_body):
    """Deploys a clean HTTP POST request following Google Workspace redirection tunnels."""
    try:
        target_webhook_url = os.environ.get("GOOGLE_SCRIPT_URL")

        if not target_webhook_url:
            return False, "Configuration Error: GOOGLE_SCRIPT_URL missing from Hugging Face settings."

        payload_data = {
            "name": recruiter_name,
            "email": recruiter_email,
            "subject": lead_subject,
            "message": lead_body
        }

        # CRITICAL FIX: Add allow_redirects=True so Python follows Google's 302 redirect pathways
        network_response = requests.post(
            target_webhook_url, 
            json=payload_data, 
            allow_redirects=True, 
            timeout=15
        )
        
        # Check for standard success codes or confirmation indicators
        if network_response.status_code == 200:
            return True, "Transmission deployed safely via Web API."
        else:
            return False, f"API Response Error (Code {network_response.status_code})"
            
    except Exception as network_exception:
        return False, f"Network mapping error: {str(network_exception)}"


# --- MAIN APP LAYOUT RENDERING ---
st.title("👨‍⚕️ Dr. Louka Abed, MD")
st.subheader("Clinical Data Scientist | International Medical Graduate")
st.write("Bridging advanced data science architectures with enterprise clinical trials compliance.")

st.divider()

# --- CONTACT FORM SECTION ---
st.markdown("### 📬 Secure Communication Gateway")
st.write("Route strategic pharmaceutical inquiries or trial architecture reviews directly to my enterprise inbox.")

# Establish atomic transactional form loop logic 
with st.form("secure_contact_gateway", clear_on_submit=True):
    col_left, col_right = st.columns(2)
    
    with col_left:
        input_name = st.text_input("Professional Name / Organization", placeholder="e.g., Pfizer Executive Search")
        input_subject = st.text_input("Project Objective / Subject Title", placeholder="e.g., Biometrics Sourcing")
    
    with col_right:
        input_email = st.text_input("Corporate Return Email Address", placeholder="name@company.com")

    input_message = st.text_area("Pipeline Scope Specifications / Message Context", placeholder="Type your inquiry details here...")
    dispatch_trigger = st.form_submit_button("Deploy Encrypted Network Transmission")

    if dispatch_trigger:
        if not input_name or not input_email or not input_message:
            st.warning("All primary communication channels require population before deployment.")
        elif "@" not in input_email:
            st.error("The parameters provided do not map to a standard structured syntax for email configurations.")
        else:
            with st.spinner("Initializing secure tunnel to Google Workspace..."):
                is_sent, status_log = transmit_pharma_lead(input_name, input_email, input_subject, input_message)
                if is_sent:
                    st.success("Success! Message safely processed by Google Workspace and routed to contact@loukaabed.com.")
                else:
                    st.error(status_log)
