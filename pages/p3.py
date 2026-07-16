import streamlit as st
import utils.ui as ui
import pandas as pd
import time

st.title('Testing Streamlit and code implementation')

dataset = ui.upload()
for file, df in dataset:
    st.write(file)
    st.write(df.head())
    time.sleep(2)

