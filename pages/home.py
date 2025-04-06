import streamlit as st

def show_home():
    """Home page content"""
    
    st.markdown("""
    ## Welcome to SHL Solutions Recommender
    
    This intelligent system helps you find the perfect SHL assessment solutions by:
    
    - 🔍 Understanding your specific needs
    - 📊 Analyzing solution characteristics
    - 📄 Extracting insights from PDF documents
    - 💡 Providing AI-powered recommendations
    
    ### Get Started
    1. Navigate to the **Search** page
    2. Enter your requirements
    3. Get personalized recommendations
    """)
    
    st.image("assets/shl-logo.png", width=200)
