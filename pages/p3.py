import streamlit as st
import utils.ui as ui

st.title('Testing Streamlit and code implementation')


dataset=ui.upload(st.session_state)
for file in dataset:
    st.write(file.name)