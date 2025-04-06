import streamlit as st
st.set_page_config(
    page_title="SHL Recommender Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
from dotenv import load_dotenv
from components.header import show_header
from components.sidebar import show_sidebar
from SHLAdvancedRecommender import SHLAdvancedRecommender
from pages.home import show_home
if not st.secrets.get("GROQ_API_KEY"):
    st.error("API key not configured")
    st.stop()
# Load environment variables
load_dotenv()

# Configure page


# Initialize recommender
@st.cache_resource
def get_recommender():
    return SHLAdvancedRecommender()

def company_info():
    """Company information section"""
    st.sidebar.markdown("---")
    # st.sidebar.markdown("""
    # **About SHL Solutions**  
    # # World leader in talent innovation  
    # # [www.shl.com](https://www.shl.com)
    # """)

# ... (previous imports remain the same)

def main():
    """Main application entry point"""
    # Initialize session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    
    # Show header only once
    show_header()
    
    # Show sidebar navigation
    show_sidebar()
    company_info()
    
    # Custom CSS
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Debugging panel
    if st.session_state.get('debug', False):
        st.sidebar.write("Session state:", st.session_state)
    
    # Page router
    if st.session_state.current_page == 'search':
        from pages.search import show_search
        show_search(get_recommender())
    elif st.session_state.current_page == 'feedback':
        from pages.feedback_analytics import show_feedback_analytics
        show_feedback_analytics()
    else:
        from pages.home import show_home
        show_home()

# ... (rest of the file remains the same)

if __name__ == "__main__":
    main()