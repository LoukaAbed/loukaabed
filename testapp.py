import streamlit as st

st.set_page_config(page_title="My App")

# Define your pages
home_page = st.Page("hello.py", title="Home", icon="🏠")
another_page = st.Page("analytics.py", title="Analytics", icon="📊")
third_page = st.Page("hellostreamlit.py", title="Hello Streamlit", icon="👋")

# Group pages and initialize navigation
# Run navigation
nav = st.navigation([home_page, another_page, third_page])

nav.run()
