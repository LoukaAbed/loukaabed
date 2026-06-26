import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Interactive SAS-Style Analytics Playground")
st.write("Upload your dataset, customize your processing parameters, and execute calculations live on Hugging Face.")

# ==========================================
# 1. USER FILE UPLOAD WIDGET
# ==========================================
st.subheader("📁 Step 1: Stage Data File")
uploaded_file = st.file_uploader("Upload a CSV dataset file to begin:", type=["csv"])

# Provide a sample dataset fallback if they don't upload a file right away
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    file_name = uploaded_file.name
else:
    # Build a fast mock "sashelp.class" dataset for testing
    df = pd.DataFrame({
        'Name': ['Alfred', 'Alice', 'Barbara', 'Carol', 'Henry', 'James', 'Jeffrey', 'John', 'Judy', 'Robert'],
        'Sex': ['M', 'F', 'F', 'F', 'M', 'M', 'M', 'M', 'F', 'M'],
        'Age': [14, 13, 13, 14, 14, 12, 13, 12, 14, 12],
        'Height': [69.0, 56.5, 65.3, 62.8, 63.5, 57.3, 62.5, 59.0, 64.3, 64.8],
        'Weight': [112.5, 84.0, 98.0, 102.5, 102.5, 83.0, 84.0, 99.5, 90.0, 128.0]
    })
    file_name = "sashelp.class (Default Demo Template)"

st.info(f"Active Data Target: `{file_name}`")

# ==========================================
# 2. INTERACTIVE PARAMETER CONTROLS & CODE WINDOW
# ==========================================
st.markdown("---")
st.subheader("🎛️ Step 2: Configure SAS Syntax Variables & Code")

# Split controls into neat grid columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Analytical Parameters:**")
    # Identify unique categorical columns to filter dynamically
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    if text_cols:
        filter_col = st.selectbox("Group / Filter Column:", text_cols)
        filter_val = st.selectbox("Select Filter Value Scope:", df[filter_col].unique())
    else:
        filter_col, filter_val = None, None
        st.caption("No categorical grouping columns detected.")

with col2:
    st.markdown("**Calculation Metrics:**")
    # Identify numeric columns for calculation targets
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if num_cols:
        target_metric = st.selectbox("Target Aggregation Variable:", num_cols)
        summary_type = st.radio("SAS Procedure Action:", ["MEAN (Average)", "SUM (Total)", "MAX (Maximum Value)"])
    else:
        target_metric, summary_type = None, None
        st.caption("No numeric calculation columns detected.")

# Display a customizable SAS Code Simulator window mapping to their inputs
st.markdown("**Simulated SAS Script Terminal Execution Input:**")
simulated_sas_code = f"""/* Auto-Generated Dynamic SAS Procedure */
PROC SUMMARY DATA=work.user_upload NWAY;
    WHERE {f"{filter_col} = '{filter_val}'" if filter_col else "1=1"};
    VAR {target_metric if target_metric else "NumericVariable"};
    OUTPUT OUT=work.analytics_results {summary_type.split()[0].lower()}=;
RUN;

PROC PRINT DATA=work.analytics_results;
RUN;"""

# Allows users to inspect or change the code visually
st.code(simulated_sas_code, language="sas")

# ==========================================
# 3. THE "PROCESS" OPERATION TRIGGER BUTTON
# ==========================================
st.markdown("---")
st.subheader("🚀 Step 3: Run Data Pipeline")

# Placing the process action trigger button right beside the parameter setups
if st.button("⚙️ Process Analytics", type="primary", use_container_width=True):
    with st.spinner("Compiling parameter states and executing data matrix mapping..."):
        
        # Apply the user parameter filters behind the scenes in Python
        processed_df = df.copy()
        if filter_col and filter_val:
            processed_df = processed_df[processed_df[filter_col] == filter_val]
            
        # Perform the requested SAS Procedure calculation
        if target_metric and summary_type:
            stat_name = summary_type.split()[0]
            if stat_name == "MEAN":
                calc_val = processed_df[target_metric].mean()
            elif stat_name == "SUM":
                calc_val = processed_df[target_metric].sum()
            else:
                calc_val = processed_df[target_metric].max()
                
            # Build a formal summary table output resembling an ODS SAS report
            summary_results_df = pd.DataFrame({
                "Analysis Variable": [target_metric],
                "Filter Condition": [f"{filter_col} == {filter_val}" if filter_col else "None"],
                f"SAS Computed {stat_name}": [round(calc_val, 2)],
                "Observation Count": [len(processed_df)]
            })
            
            # --- DISPLAY OUTPUT RESULTS & TABLES ---
            st.success("✅ Output calculations completed successfully!")
            
            tab1, tab2 = st.tabs(["📊 SAS ODS Output Table", "📈 Analytical Chart"])
            
            with tab1:
                st.markdown(f"### The SAS System: `PROC SUMMARY` Results")
                st.dataframe(summary_results_df, hide_index=True, use_container_width=True)
                
                st.markdown("### Filtered Base Observations Subset")
                st.dataframe(processed_df, use_container_width=True)
                
            with tab2:
                st.markdown(f"### Distribution Map of {target_metric}")
                # Render a bar graph of their specific column subset data values
                if len(processed_df) > 0:
                    st.bar_chart(processed_df, y=target_metric)
                else:
                    st.warning("Not enough subset rows to map a chart curve.")
        else:
            st.error("Cannot execute calculations without valid matching dataset metrics.")
