import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def transmit_pharma_lead(recruiter_name, recruiter_email, lead_subject, lead_body):
    """Establishes an explicit secure TLS layer handshake over Google Workspace SMTP relays."""
    try:
        # Load credentials directly from secure runtime secrets dictionary mapping
        smtp_target_host = st.secrets["email_server"]["smtp_server"]
        smtp_target_port = st.secrets["email_server"]["port"]
        authenticated_user = st.secrets["email_server"]["sender_email"]
        app_specific_token = st.secrets["email_server"]["password"]

        # Formulate explicit multi-part MIME payload headers
        email_payload = MIMEMultipart()
        email_payload['From'] = authenticated_user
        email_payload['To'] = authenticated_user  # Route incoming requests to your inbox
        email_payload['Reply-To'] = recruiter_email
        email_payload['Subject'] = f"💼 Pharma Recruiting: {lead_subject}"

        # Clean string layout structural formatting
        formatted_message = (
            f"Sender Name / Title: {recruiter_name}\n"
            f"Direct Return Route: {recruiter_email}\n\n"
            f"Message Body:\n{lead_body}"
        )
        email_payload.attach(MIMEText(formatted_message, 'plain', 'utf-8'))

        # Instantiate dedicated socket connection mapping to Google Workspace relays
        network_socket = smtplib.SMTP(smtp_target_host, smtp_target_port)
        network_socket.ehlo()  # Explicitly ping host to announce client capabilities
        network_socket.starttls()  # Encrypt session context traffic natively 
        network_socket.ehlo()
        
        # Authenticate session utilizing your unique Google App Password context
        network_socket.login(authenticated_user, app_specific_token)
        
        # Dispatch traffic across the established link structure
        network_socket.sendmail(authenticated_user, authenticated_user, email_payload.as_string())
        network_socket.quit()
        return True, "Transmission deployed safely."
        
    except smtplib.SMTPAuthenticationError:
        return False, "Google Workspace authentication failed. Confirm your 16-character App Password."
    except Exception as network_exception:
        return False, f"Network initialization anomaly encountered: {str(network_exception)}"

# --- STREAMLIT GRAPHICAL RENDERING LAYER ---
st.title("📬 Connect to Dr. Louka Abed's Desk")
st.write("Route strategic pharmaceutical inquiries or trial architecture reviews directly to my enterprise inbox.")

# Establish atomic transactional form loop logic 
with st.form("secure_contact_gateway", clear_on_submit=True):
    col_left, col_right = st.columns(2)
    
    with col_left:
        input_name = st.text_input("Professional Name / Organization")
        input_subject = st.text_input("Project Objective / Subject Title")
    
    with col_right:
        input_email = st.text_input("Corporate Return Email Address")

    input_message = st.text_area("Pipeline Scope Specifications / Message Context")
    dispatch_trigger = st.form_submit_button("Deploy Encrypted Network Transmission")

    if dispatch_trigger:
        if not input_name or not input_email or not input_message:
            st.warning("All primary communication channels require population before deployment.")
        elif "@" not in input_email:
            st.error("The parameters provided do not map to a standard structured syntax for email configurations.")
        else:
            with st.spinner("Initializing cryptographic pipeline to Google Workspace relays..."):
                is_sent, status_log = transmit_pharma_lead(input_name, input_email, input_subject, input_message)
                if is_sent:
                    st.success("Success! Message safely intercepted by Google Workspace and routed to contact@loukaabed.com.")
                else:
                    st.error(status_log)
