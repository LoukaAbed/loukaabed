import streamlit as st
import utils.ui as ui

st.title('Testing Streamlit and code implementation')

dataset = ui.upload()
st.write(dataset)

