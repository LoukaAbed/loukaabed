import streamlit as st
import pandas as pd

st.title("📊 SAS Portfolio Analytics Engine")
st.write("This workspace visualizes pre-compiled datasets extracted directly from your SAS environment.")

try:
    # Read the dataset exported from your SAS platform environment
    df = pd.read_csv("portfolio_summary.csv")
    
    st.success("✅ SAS Datasets loaded successfully!")
    
    # Showcase standard summary matrices or interactive data selections
    selected_make = st.selectbox("Filter by Manufacturer:", df['Make'].unique())
    filtered_df = df[df['Make'] == selected_make]
    
    # Display the clean analytics metrics matrix
    st.subheader(f"Metrics Overview for {selected_make}")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Render native Streamlit charts using your SAS data points
    st.subheader("Performance Comparison Chart")
    st.bar_chart(filtered_df, x="Type", y="Horsepower")
    
except FileNotFoundError:
    st.error("❌ The data file 'portfolio_summary.csv' could not be found.")
    st.info("💡 Make sure you upload your exported SAS CSV file to the root of your GitHub repository.")
except Exception as e:
    st.error(f"An unexpected data parsing error occurred: {e}")
