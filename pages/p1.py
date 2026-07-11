from pydoc import text
import streamlit as st
import utils.db_utils as db

st.title("Neon Database Connection Test")
st.divider()

uploaded_file = st.file_uploader("Upload a CSV file: Max Size 2MB", type=["csv"])
if uploaded_file is not None:
    if uploaded_file.size > 2 * 1024 * 1024:
        st.error("File size exceeds the maximum limit of 2MB.")
        st.stop()
    tbl_name = db.store_db(uploaded_file)
    st.success(f"Your file {uploaded_file.name} was uploaded and stored in database as: {tbl_name}")
    uploadedfile_preview = f"SELECT * FROM {tbl_name} LIMIT 5"
    st.write(db.fetch_db(uploadedfile_preview))
    

query = "SELECT * FROM bp where gender = :gender and age > :age"
st.write(db.fetch_db(query, {"gender": "Male", "age": 25}))

st.divider()
min_age, max_age = st.slider("Age", 0.0, 100.0, value=(0.0, 100.0), key="age")
query_age = "SELECT * FROM bp where gender = :gender and age between :min_age and :max_age"
gender = st.radio(label="Gender", options=["Male", "Female"], horizontal=True)
st.write(db.fetch_db(query_age, {"gender": gender, "min_age": min_age, "max_age": max_age}))
