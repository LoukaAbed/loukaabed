import streamlit as st

st.title("👋 SAS Experience Workspace")
st.write("This workspace interacts with your live **SAS OnDemand for Academics (ODA)** cloud environment.")

# 1. Verify if the global SAS connection is available in memory
if "sas_conn" in st.session_state and st.session_state["sas_conn"] is not None:
    sas_session = st.session_state["sas_conn"]
    
    st.markdown("---")
    st.subheader("🤖 Interactive SAS Code Sandbox")
    st.write("Modify the SAS script below and hit **Execute** to run it live on the cloud server.")
    
    # 2. Provide an interactive text area with a default demo script
    default_sas_code = """/* Default Demo Query */
proc print data=sashelp.cars(obs=5);
    var make model type horsepower msrp;
run;"""

    sas_code = st.text_area(
        label="Write your custom SAS code here:", 
        value=default_sas_code, 
        height=180
    )
    
    # 3. Add an execution submission trigger button
    if st.button("🚀 Execute Code Block", type="primary"):
        with st.spinner("Streaming calculations to SAS cloud nodes..."):
            try:
                # Submit the code to SAS
                res = sas_session.submit(sas_code)
                
                # 4. Use horizontal layout tabs to neatly organize the output
                tab1, tab2 = st.tabs(["📊 ODS HTML Results", "📜 SAS System Log"])
                
                with tab1:
                    if res.get('LST'):
                        st.html(res['LST'])  # Renders beautiful native SAS tables
                    else:
                        st.info("Query processed, but no output data table (LST) was generated.")
                        
                with tab2:
                    if res.get('LOG'):
                        st.code(res['LOG'], language="sas") # Displays operational steps and errors
                    else:
                        st.error("No log output returned from server.")
                        
            except Exception as e:
                st.error(f"An unexpected script parsing error occurred: {e}")

else:
    # 5. Fallback protection UI if the user bypassed the landing page connection
    st.error("❌ No active SAS session detected.")
    st.warning("Please navigate back to the Home page first to securely establish the backend cloud authorization pipeline.")
