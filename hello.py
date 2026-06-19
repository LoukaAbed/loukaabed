import streamlit as st
import requests  # Native web protocol engine
import os

def transmit_pharma_lead(recruiter_name, recruiter_email, lead_subject, lead_body):
    """Deploys a clean HTTP POST request over standard web ports to your Google relay."""
    try:
        # Fetch your private webhook link from Hugging Face environment variables
        target_webhook_url = os.environ.get("GOOGLE_SCRIPT_URL")

        if not target_webhook_url:
            return False, "Configuration Error: GOOGLE_SCRIPT_URL missing from Hugging Face settings."

        # Package the form variables cleanly into a standard web data frame
        payload_data = {
            "name": recruiter_name,
            "email": recruiter_email,
            "subject": lead_subject,
            "message": lead_body
        }

        # Fire the data out over standard web port 443 (Allowed by Hugging Face)
        network_response = requests.post(target_webhook_url, json=payload_data, timeout=10)
        
        if network_response.status_code == 200 and "Success" in network_response.text:
            return True, "Transmission deployed safely via Web API."
        else:
            return False, f"Server Error: Encountered communication failure on endpoint node."
            
    except Exception as network_exception:
        return False, f"Network mapping error: {str(network_exception)}"
