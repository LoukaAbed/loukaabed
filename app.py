import streamlit as st

# set config for all subpages
st.set_page_config(
    page_title='Louka Abed | Portfolio',
    page_icon='assets/Louka_portfolio_tab_icon.png',
    layout='wide'
)

# Define page navigation
contact = st.Page("pages/contact.py", title="Contact", icon="📬", url_path='Contact')
p1 = st.Page("pages/p1.py", title="Project 1", icon="📈", url_path='Project1')
#p2 = st.Page("pages/p2.py", title="Project 2", icon="📈", url_path='Project2')
# Run navigation 
nav = st.navigation([contact, p1])
nav.run()
