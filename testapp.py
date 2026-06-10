import streamlit as st

# 1. Configure page settings
st.set_page_config(
    page_title="Dr. Portfolio | Clinical Data Scientist", 
    page_icon="🧬", 
    layout="wide"
)

# 2. Main layout columns for Personal Photo and Bio
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Replace with your actual local photo file pathway or an online image URL
    st.image(
        "https://placeholder.com", 
        caption="IMG & Clinical Data Scientist", 
        use_container_width=True
    )
    st.markdown("### 🎯 Career Objective")
    st.info(
        "Leveraging clinical insights and advanced data science to accelerate "
        "clinical trials, optimize drug discovery pipelines, and deliver high-impact "
        "statistical solutions within the global pharmaceutical sector."
    )

with col2:
    st.title("Welcome to My Professional Portfolio")
    st.subheader("International Medical Graduate & Clinical Data Scientist")
    
    st.markdown("""
    #### 🎓 Education
    * **Master of Science in Data Science (Accelerated Track)** | *Eastern University*
    * **Doctor of Medicine (M.D.) / International Medical Graduate**
    
    #### 🔬 Executive Value Proposition
    Bridging the gap between complex physiological insights and scalable predictive algorithms. 
    Specialized in processing large-scale electronic health records (EHR), biological data, 
    and structured clinical trial datasets to power pharmaceutical innovation.
    """)
    
    # Quick navigation guidance
    st.success("👈 **Use the sidebar navigation** to explore my Python & R projects, view my CV, or get in touch.")
