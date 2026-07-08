import os
import streamlit as st
import sqlalchemy
from sqlalchemy import create_engine

st.title("📈 Test database")

# 1. Fetch the secure Neon URL from Hugging Face Secrets
db_url = os.environ.get("NEON_DB_URL")

if not db_url:
    st.error("Missing NEON_DB_URL secret in Hugging Face settings.")
else:
    try:
        # 2. Establish a connection engine via SQLAlchemy
        engine = create_engine(db_url)
        
        # 3. Run a basic check query to ensure everything is working
        with engine.connect() as conn:
            # Executes a lightweight internal check query
            result = conn.execute(sqlalchemy.text("SELECT 1;"))
            
        st.success("Successfully connected to your Neon Postgres Database!")
        
    except Exception as e:
        st.error(f"Database Connection Error: {e}")


