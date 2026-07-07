import base64
import mimetypes
import os
import requests  # web traffic through google script
import streamlit as st

# --- CORRECT INACCURATE 200MB DISPLAY  on streamlit attachment button---
st.markdown(
    """
    <style>
    /* 1. correct container wrapper to remove 200MB label */
    div[data-testid="stFileUploaderDropzoneInstructions"] > div > small {
        display: none !important;
    }
    
    /* 2. correct fallback label wrappers if present */
    div[data-testid="stFileUploaderDropzoneInstructions"] > div > span {
        display: none !important;
    }
    
    /* 3. Showing Accurate File Uploader Size */
    div[data-testid="stFileUploaderDropzoneInstructions"] > div::after {
        content: "Limit Max Upload Size 25MB";
        display: block;
        font-size: 0.8rem;
        color: #666666;
        margin-top: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def contact(name, email, subject, body, attachments_list=None):
    """Email delivery routing via Google Script webhook with multi-file list payload integration."""
    try:
        google_script = os.environ.get("GOOGLE_SCRIPT_URL")

        if not google_script:
            return False, "System Configuration Error: API Endpoint Missing."

        message_data = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": body,
            "attachments": attachments_list if attachments_list else [],
        }

        # Expanded timeout to 30 seconds to support multiple heavy data packets over the network
        network_response = requests.post(
            google_script, json=message_data, allow_redirects=True, timeout=30
        )

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
left, center, right = st.columns([3, 2, 3])
with center:
    st.title("Louka Abed")
st.subheader("Clinical Data Scientist | AI Translational Medicine & Pharma R&D")
st.write("""International Medical Graduate (MD) combining clinical and biochemistry domain expertise with MS in Data Science and Mathematics foundations to validate, 
audit, model, and extract AI insights—accelerating novel drug discovery and building predictive translational medicine pipelines through a systems approach 
that integrates complex healthcare data streams, high-throughput genomic and proteomic registries, and heterogeneous multiomics architectures.""")

st.divider()

# --- CONTACT FORM SECTION ---
st.markdown("### 📬 Contact & Inquiries")
st.markdown(
    "For professional inquiries, please submit a message below or email directly at [contact@loukaabed.com](mailto:contact@loukaabed.com)."
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

    uploaded_files = st.file_uploader(
        "Upload Attachments (Any File Type - Max Total 25MB)",
        accept_multiple_files=True,
        help="Attach datasets, medical images, Python (.py) / R (.r) scripts, PDFs, text, docx.",
    )

    dispatch_trigger = st.form_submit_button("Submit Message Securely")

    if dispatch_trigger:
        if not name or not email or not message:
            st.warning("Please complete all core form fields before submitting.")
        elif "@" not in email or "." not in email:
            st.error("Please provide a valid email format.")
        else:
            # Informative spinner text aligned with security and clinical architecture
            with st.spinner("Encrypting data and initializing secure transfer..."):

                attachments_payload = []
                cumulative_size = 0

                if uploaded_files:
                    for uploaded_file in uploaded_files:
                        cumulative_size += uploaded_file.size

                        if cumulative_size > 25 * 1024 * 1024:
                            st.error(
                                "Total combined file sizes exceeded. 25MB is maximum allowed."
                            )
                            st.stop()

                        file_bytes = uploaded_file.read()
                        uploaded_file.seek(0)
                        base64_encoded = base64.b64encode(file_bytes).decode("utf-8")
                        
                        guessed_type, _ = mimetypes.guess_type(uploaded_file.name)
                        inferred_mime = guessed_type or "application/octet-stream"

                        attachments_payload.append(
                            {
                                "bytes": base64_encoded,
                                "filename": uploaded_file.name,
                                "mime_type": inferred_mime,
                            }
                        )

                is_sent, status_log = contact(
                    name, email, subject, message, attachments_payload
                )
                if is_sent:
                    st.success(
                        "Your message was sent successfully to contact@loukaabed.com. Thank you."
                    )
                else:
                    st.error(status_log)
