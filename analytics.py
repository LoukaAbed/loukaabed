import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("💻 Advanced SAS Studio Collaborative Sandbox")
st.write("Upload custom files or execute code blocks directly inside the embedded SAS processing engine.")

# Create interface sidebars/tabs to manage data distribution
upload_tab, editor_tab = st.tabs(["📁 Local Data Stage", "🖥️ Active SAS Studio Interface"])

with upload_tab:
    st.subheader("Bring Your Own Data File")
    st.write("Want to work on a custom file? Upload it below to inspect its variables before sending it to SAS.")
    
    uploaded_file = st.file_uploader("Upload a CSV or Excel dataset:", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            # Parse the user file locally in Python for immediate inspection
            if uploaded_file.name.endswith('.csv'):
                user_df = pd.read_csv(uploaded_file)
            else:
                user_df = pd.read_excel(uploaded_file)
                
            st.success(f"Successfully processed '{uploaded_file.name}' locally!")
            
            # Show a data preview so they can confirm column names
            st.dataframe(user_df.head(5), use_container_width=True)
            
            # Provide explicitly generated copy-paste SAS snippet templates based on their file name
            st.info("💡 **Next Step to Analyze This in SAS:**")
            st.markdown(f"""
            1. Look at the **SAS Studio Interface** tab.
            2. Upload your `{uploaded_file.name}` file using the sidebar **Upload** icon.
            3. Copy and paste the following snippet into your code window to instantly process it:
            """)
            
            sas_template_code = f"""/* Copy-Paste Code Snippet Template */
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

with editor_tab:
    # Render the full interactive SAS Studio platform application environment
    sas_studio_url = "https://sas.com"
    
    st.components.v1.iframe(
        url=sas_studio_url, 
        height=850, 
        scrolling=True
    )
