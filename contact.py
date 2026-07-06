import os
import requests  # web traffic through google script
import streamlit as st

# Set page configuration at the absolute top to prevent rendering crashes
st.set_page_config(
    page_title="Louka Abed | Clinical Data Scientist & AI Translational Medicine",
    layout="wide",
    initial_sidebar_state="expanded",
)


def contact(name, email, subject, body):
    """Email delivery routing via Google Script webhook."""
    try:
        google_script = os.environ.get("GOOGLE_SCRIPT_URL")

        if not google_script:
            return False, "System Configuration Error: API Endpoint Missing."

        message_data = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": body,
        }

        # Send email through google script
        network_response = requests.post(
            google_script, json=message_data, allow_redirects=True, timeout=15
        )

        # Evaluate gateway server status
        if network_response.status_code == 200:
            return True, "Success"
        else:
            return (
                False,
                f"Gateway Server Error (HTTP Code {network_response.status_code})",
            )

    except Exception as network_exception:
        return (
            False,
            f"Secure pipeline initialization failed: {str(network_exception)}",
        )


# --- MAIN APP LAYOUT ---
st.title("Louka Abed")
st.subheader("Clinical Data Scientist & AI Translational Medicine")

# three liner summary
st.markdown(
    """International Medical Graduate (MD) combining clinical and biochemistry domain expertise 
with MS in Data Science and Mathematics foundations to validate, audit, model, and extract AI 
insights from complex healthcare data streams to accelerate novel drug discovery and build 
predictive translational medicine pipelines."""
)


st.divider()

# --- CONTACT FORM SECTION ---
st.markdown("### 📬 Contact & Inquiries")
st.markdown(
    "For professional inquiries, "
    "please submit a message below or contact me directly via [contact@loukaabed.com](mailto:contact@loukaabed.com)."
)


# Establish atomic transactional form loop logic
with st.form("contact_form", clear_on_submit=True):
    col_left, col_right = st.columns(2)

    with col_left:
        name = st.text_input(
            "Name / Organization",
            placeholder="e.g., Pharma Talent Acquisition",
        )
        subject = st.text_input(
            "Subject", placeholder="e.g., Recruitment / Collaboration"
        )

    with col_right:
        email = st.text_input(
            "Return Email Address", placeholder="name@organization.com"
        )

    message = st.text_area(
        "Message", placeholder="Provide inquiry details here..."
    )
    dispatch_trigger = st.form_submit_button("Submit Message")

    if dispatch_trigger:
        if not name or not email or not message:
            st.warning("Please complete all core form fields before submitting.")
        elif "@" not in email or "." not in email:
            st.error("Please provide a valid email format.")
        else:
            with st.spinner("Processing request..."):
                is_sent, status_log = contact(name, email, subject, message)
                if is_sent:
                    st.success(
                        "Your message was sent successfully to contact@loukaabed.com. Thank you."
                    )
                else:
                    st.error(status_log)
