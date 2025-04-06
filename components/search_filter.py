
import streamlit as st

def show_search_filters():
    """Enhanced search filters component"""
    st.sidebar.header("🔍 Refine Search")
    
    # Job Level Filter
    job_level = st.sidebar.selectbox(
        "Job Level",
        ["Any", "Entry-level", "Mid-level", "Senior", "Executive"],
        index=0
    )
    
    # Language Filter
    language = st.sidebar.selectbox(
        "Language",
        ["English", "Spanish", "French", "German", "Chinese", "Multilingual"],
        index=0
    )
    
    # Test Type Filter
    test_type = st.sidebar.selectbox(
        "Test Type",
        ["Any", "Knowledge", "Skills", "Behavioral", "Situational", "Cognitive"],
        index=0
    )
    
    # Completion Time Filter
    completion_time = st.sidebar.slider(
        "Max Completion Time (minutes)",
        min_value=10,
        max_value=120,
        value=60,
        step=5
    )
    
    return {
        "job_level": None if job_level == "Any" else job_level.lower(),
        "language": None if language == "Any" else language.lower(),
        "test_type": None if test_type == "Any" else test_type.lower(),
        "completion_time": completion_time
    }