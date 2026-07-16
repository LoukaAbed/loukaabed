import streamlit as st
import utils.ui as ui
import pandas as pd
import time

st.title('Testing Streamlit and code implementation')

ui.upload()
dataset=st.session_state['dataset_dic']
for file in dataset:
    st.write(file)
    st.write(dataset[file].head())

