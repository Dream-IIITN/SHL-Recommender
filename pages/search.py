import streamlit as st
from components.feedback import collect_feedback
from components.search_filter import show_search_filters
import time

def show_search(recommender):
    """Search interface with recommender integration"""
    st.title("🔍 Find SHL Solutions")
    
    # Debugging: Show current state
    if st.toggle("Show debug info", False):
        st.write("Current session state:", st.session_state.get('current_page', 'Not set'))
    
    # Search form
    with st.form(key="main_search_form"):
        query = st.text_area(
            "Describe your assessment needs:",
            placeholder="e.g. 'I need a data entry test for entry-level candidates...'",
            height=100,
            key="search_query"
        )
        
        # Get filters from sidebar component
        filters = show_search_filters()
        
        submitted = st.form_submit_button("Find Solutions", type="primary", use_container_width=True)
    
    # Handle search
    if submitted:
        if not query:
            st.warning("Please describe your assessment needs before searching")
            st.stop()
            
        with st.spinner("🔍 Analyzing your requirements and finding the best solutions..."):
            try:
                # Add small delay to ensure spinner shows
                time.sleep(0.1)
                
                # Call recommender
                results = recommender.recommend_solution(
                    user_query=query,
                    user_language=filters.get('language', 'english')
                )
                
                # Store results in session state
                st.session_state.last_results = results
                st.session_state.last_query = query
                
                if not results.get("response"):
                    st.error("No results found. Please try different search terms.")
                    st.stop()
                
                # Display results
                st.success("Found matching solutions!")
                st.divider()

                 # Main recommendation
                with st.container():
                    st.markdown("### 🏆 Best Match Recommendation")
                    st.markdown(results["response"])
                
                # Reasoning in expander
                if results.get("reasoning"):
                    with st.expander("🧠 See Detailed Reasoning"):
                        st.markdown(results["reasoning"])
                
               
                
                # Sources
                if results.get("sources"):
                    with st.expander("📚 View Source References", expanded=True):
                        for source in results["sources"]:
                            col1, col2 = st.columns([2, 1])
                            with col1:
                                st.markdown(f"**{source['type'].title()}**: {source.get('title', 'N/A')}")
                            with col2:
                                if source.get('url'):
                                    st.markdown(f"[View Details]({source['url']})", unsafe_allow_html=True)
                
                # Feedback
                collect_feedback()
                
            except Exception as e:
                st.error(f"Search failed: {str(e)}")
                if st.toggle("Show technical details", False):
                    st.exception(e)
                st.stop()