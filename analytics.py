import streamlit as st
import pandas as pd

# 1. Page Configuration
st.title("🖥️ Collaborative SAS Portfolio Workspace")
st.write("Upload custom files locally or execute advanced analytical modeling on your SAS cloud node.")

# 2. Layout Structure using View Tabs
upload_tab, workspace_tab = st.tabs(["📁 Local Data Stage", "🚀 Direct SAS Engine Launcher"])

with upload_tab:
    st.subheader("Bring Your Own Data File")
    st.write("Upload a dataset below to pre-process its schema and structures in Python.")
    
    uploaded_file = st.file_uploader("Upload a CSV or Excel dataset:", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            # Parse the user file locally
            if uploaded_file.name.endswith('.csv'):
                user_df = pd.read_csv(uploaded_file)
            else:
                user_df = pd.read_excel(uploaded_file)
                
            st.success(f"Successfully processed '{uploaded_file.name}' locally!")
            
            # Show data preview
            st.dataframe(user_df.head(5), use_container_width=True)
            
            # Generate copy-paste SAS snippet templates based on file metadata
            st.info("💡 **Next Step to Analyze This in SAS:**")
            st.markdown(f"""
            1. Click the **Direct SAS Engine Launcher** tab above.
            2. Launch your personal cloud workspace.
            3. Upload your `{uploaded_file.name}` file into your SAS Server files panel.
            4. Copy and paste the following snippet into your program window to compute your models:
            """)
            
            sas_template_code = f"""/* Auto-Generated SAS Import Template */
proc import datafile="~/{uploaded_file.name}" 
    out=work.my_custom_data
    dbms={"CSV" if uploaded_file.name.endswith(".csv") else "XLSX"} replace;
    getnames=yes;
run;

proc contents data=work.my_custom_data; 
run;"""
            st.code(sas_template_code, language="sas")
            
        except Exception as e:
            st.error(f"Error structuring data preview: {e}")

with workspace_tab:
    st.subheader("Launch Cloud Analytical Sandbox")
    st.write("""Because SAS ODA enforces secure web isolation policies (`X-Frame-Options`), 
    it cannot be embedded inside an inline window. Click the link button below to launch your 
    fully authenticated cloud compiler directly on SAS Institute's processing servers.""")
    
    # Target your specific Region 2 assigned workspace domain link
    sas_studio_url = "https://sas.com"
    
    # Visual Call to Action Button Layout
    st.markdown("---")
    st.link_button(
        label="👉 Open Interactive SAS Studio Application Workspace", 
        url=sas_studio_url, 
        type="primary",
        use_container_width=True
    )
    st.markdown("---")
