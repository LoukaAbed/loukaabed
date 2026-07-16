import streamlit as st
import utils.ui as ui
import pandas as pd
import time

st.title('Testing Streamlit and code implementation')

dataset = ui.upload()
for file in dataset:
    st.write(file)
    st.write(dataset[file].head())
    time.sleep(2)

