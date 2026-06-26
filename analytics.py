import streamlit as st
import pandas as pd

st.title("📊 Customized SAS Analytics Dashboard")
st.write("Filter, edit, and format your pre-compiled SAS portfolio datasets live.")

try:
    # Load the base SAS dataset from your repository
    df = pd.read_csv("portfolio_summary.csv")
    st.success("✅ SAS Dataset synchronized successfully!")
    st.markdown("---")

    # ==========================================
    # 1. CUSTOMIZE CODE INPUTS & FILTERS
    # ==========================================
    st.subheader("🛠️ Workspace Controls")
    
    # Use layout columns to place input filters side-by-side
    col1, col2 = st.columns(2)
    with col1:
        selected_make = st.selectbox("Select Manufacturer:", sorted(df['Make'].unique()))
    with col2:
        # Numeric input slider to filter by baseline performance thresholds
        min_horsepower = st.slider("Minimum Horsepower Threshold:", 
                                   int(df['Horsepower'].min()), 
                                   int(df['Horsepower'].max()), 
                                   int(df['Horsepower'].mean()))

    # Apply the user inputs directly to filter the SAS DataFrame
    filtered_df = df[(df['Make'] == selected_make) & (df['Horsepower'] >= min_horsepower)]

    # ==========================================
    # 2. CUSTOMIZE OUTPUT DATA GRID & TABLES
    # ==========================================
    st.subheader(f"📈 Formatted Metrics Matrix: {selected_make}")
    
    if not filtered_df.empty:
        # Use st.dataframe along with column_config to explicitly format data fields
        st.dataframe(
            filtered_df,
            use_container_width=True, # Forces table to fit screen neatly
            hide_index=True,          # Removes the messy default row index numbers
            column_config={
                "Make": st.column_config.TextColumn("Brand Title"),
                "Type": st.column_config.TextColumn("Vehicle Category"),
                "Horsepower": st.column_config.NumberColumn("Engine HP", format="%d HP"),
                "MSRP": st.column_config.NumberColumn("Market Price (USD)", format="$%,.2f"),
                "MPG_City": st.column_config.NumberColumn("City Economy", format="%d MPG"),
                "MPG_Highway": st.column_config.NumberColumn("Highway Economy", format="%d MPG"),
            }
        )
        
        # ==========================================
        # 3. ADVANCED: ADD AN EDITABLE DATA INPUT TABLE
        # ==========================================
        st.markdown("---")
        st.subheader("📝 Interactive Sandbox Data Editor")
        st.write("Double-click cells below to change values directly in your browser session:")
        
        # st.data_editor creates a fully editable copy of your table
        edited_df = st.data_editor(
            filtered_df, 
            use_container_width=True,
            hide_index=True,
            key="sas_data_editor"
        )
        
        # ==========================================
        # 4. CUSTOMIZE GRAPHICAL OUTPUT RESULTS
        # ==========================================
        st.markdown("---")
        st.subheader("📊 Visual Performance Charts")
        
        tab1, tab2 = st.tabs(["Engine Power Matrix", "Fuel Efficiency Curve"])
        with tab1:
            # Render a clean bar chart mapping the edited dataset points
            st.bar_chart(edited_df, x="Type", y="MSRP", color="#0379ce")
        with tab2:
            # Render a line chart comparing city vs highway metrics
            st.line_chart(edited_df, x="Type", y=["MPG_City", "MPG_Highway"])
            
    else:
        st.warning("No data points found matching your current filter criteria thresholds.")
    
except FileNotFoundError:
    st.error("❌ The data file 'portfolio_summary.csv' could not be found.")
except Exception as e:
    st.error(f"An unexpected data parsing error occurred: {e}")
