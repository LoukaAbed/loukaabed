import streamlit as st
import utils.db as db
import utils.ui as ui

st.title("Testing usage of data from a database")
st.divider()
ui.maxfile_size(2) #change default displayed file size from 200MB to 2MB

st.subheader("Implementing user-driven interactive data filter")

min_age, max_age = st.slider("Age", 0.0, 100.0, value=(0.0, 100.0), key="age")
query_age = "SELECT * FROM bp where gender = :gender and age between :min_age and :max_age"
gender = st.radio(label="Gender", options=["Male", "Female"], horizontal=True)
parameter={"gender": gender, "min_age": min_age, "max_age": max_age}
st.write(db.fetch_db(query_age, parameter))

st.divider()

st.subheader("User upload file into database, read data, then delete. Will apply data science tools in future iteration. try it!")

#using form to prevent db write from random clicks
with st.form('batch_files_upload', clear_on_submit=False):
    dataset = st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key='dataset_key')
    upload_button = st.form_submit_button('Upload Dataset')




if upload_button:
    if not dataset:
        st.warning('To upload, please add files first to uploader')
    else:
        with st.spinner('Uploading your files to public schema, processing...'):
            tables = db.dataset_db(dataset, schema='public')
            if tables:
                st.success(f"Originally {len(dataset)} files uploaded and {len(tables)} tables saved successfully in public schema db")
                for tbl_name, table in tables.items():
                    st.code(f"Tables Saved to the database: {tbl_name} with  {len(table)} rows")
            else:
                st.warning("File types are not supported, only accept csv xlsx tsv txt")
st.space('large')