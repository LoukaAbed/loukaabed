import streamlit as st
import utils.db as db
import utils.ui as ui

st.title("Testing usage of data from a database")

st.divider()

#change default displayed file size from 200MB to 2MB
ui.maxfile_size(2)

st.subheader("Implementing user-driven interactive data filter")

min_age, max_age = st.slider("Age", 0.0, 100.0, value=(0.0, 100.0), key="age")
query_age = "SELECT * FROM bp where gender = :gender and age between :min_age and :max_age"
gender = st.radio(label="Gender", options=["Male", "Female"], horizontal=True)
st.write(db.fetch_db(query_age, {"gender": gender, "min_age": min_age, "max_age": max_age}))

st.divider()

st.subheader("Upload user file into database, retrieve and clean database. Will apply data science tools in future iteration ")


if 'active_tbl' not in st.session_state:
    st.session_state['active_tbl'] = None
if 'version' not in st.session_state:
    st.session_state['version']=0
uploader_key=f"upload_{st.session_state['version']}"
uploaded_file = st.file_uploader("Upload a CSV file: Max Size 2MB", type=["csv"], key=uploader_key)

if 'deletion_msg' not in st.session_state:
    st.session_state['deletion_msg']=False
if 'deleted_tbl' not in  st.session_state:
    st.session_state['deleted_tbl']=''

if st.session_state['deletion_msg']:
    st.success(f'Your uploaded file {st.session_state['deleted_tbl']} has been successfuly deleted from the database')
    st.session_state['deletion_msg']=False
    st.session_state['deleted_tbl']=''

if uploaded_file is not None:
    if uploaded_file.size > 2 * 1024 * 1024:
        st.error("File size exceeds the maximum limit of 2MB.")
        st.stop()
    if st.session_state['active_tbl'] is None:
        tbl_name = db.store_db(uploaded_file, prefix='', tbl_name=uploaded_file.name)
        st.session_state['active_tbl']=tbl_name
        st.success(f"Your file {uploaded_file.name.replace(' ', '_')} was uploaded and stored in database as: {tbl_name}")
if st.session_state['active_tbl'] is not None:
    tbl_name = st.session_state['active_tbl']
    uploadedfile_preview = f"SELECT * FROM {tbl_name} LIMIT 5"
    st.write(db.fetch_db(uploadedfile_preview))
    if st.button("Delete Uploaded Table From Our Database"):
        db.drop_db(tbl_name)
        st.session_state['deletion_msg']=True
        st.session_state['deleted_tbl']=tbl_name
        st.session_state['active_tbl'] = None
        st.session_state['version'] +=1
        st.rerun()

st.space('large')