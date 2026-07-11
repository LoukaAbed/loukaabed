from pydoc import text
import streamlit as st
import utils.db_utils as db

st.title("Database Connection and Management Test")
st.divider()

if 'uploaded_file' not in st.session_state:
    st.session_state['active_tbl'] = None

uploaded_file = st.file_uploader("Upload a CSV file: Max Size 2MB", type=["csv"])
if uploaded_file is not None:
    if uploaded_file.size > 2 * 1024 * 1024:
        st.error("File size exceeds the maximum limit of 2MB.")
        st.stop()
    if st.session_state['uploaded_file'] is None:
        st.session_state['active_tbl'] = db.store_db(uploaded_file)
        st.session_state['uploaded_file'] = st.session_state['active_tbl']
        st.success(f"Your file {uploaded_file.name.replace(' ', '_')} was uploaded and stored in database as: {tbl_name}")
if st.session_state['active_tbl'] is not None:
    uploadedfile_preview = f"SELECT * FROM {st.session_state['active_tbl']} LIMIT 5"
    st.write(db.fetch_db(uploadedfile_preview))
    if st.button("Drop Uploaded Table"):
        db.drop_db(st.session_state['active_tbl'])
        st.success(f"Table {st.session_state['active_tbl']} has been dropped from the database.")
        st.session_state['active_tbl'] = None
        st.rerun()

st.divider()
min_age, max_age = st.slider("Age", 0.0, 100.0, value=(0.0, 100.0), key="age")
query_age = "SELECT * FROM bp where gender = :gender and age between :min_age and :max_age"
gender = st.radio(label="Gender", options=["Male", "Female"], horizontal=True)
st.write(db.fetch_db(query_age, {"gender": gender, "min_age": min_age, "max_age": max_age}))
