import streamlit as st

def show_sidebar():
    """Sidebar navigation with proper state management"""
    with st.sidebar:
        st.title("Navigation")
        
        # Use radio buttons for clear page selection
        page = st.radio(
            "Go to",
            ["🏠 Home", "🔍 Search Solutions", "📊 Feedback"],
            index=0 if st.session_state.get('current_page') == 'home' else 1,
            label_visibility="collapsed"
        )
        
        # Update session state based on selection
        if page == "🏠 Home":
            st.session_state.current_page = 'home'
        elif page == "🔍 Search Solutions":
            st.session_state.current_page = 'search'
        else:
            st.session_state.current_page = 'feedback'