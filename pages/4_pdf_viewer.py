import streamlit as st
from services.recommender import SHLRecommender

def show_pdf_viewer():
    st.title("📄 PDF Content Viewer")
    
    if 'last_results' not in st.session_state:
        st.warning("Please perform a search first")
        return
    
    if not st.session_state.last_results.get("pdf_available"):
        st.info("No PDF content available for these results")
        return
    
    selected_solution = st.selectbox(
        "Select solution to view PDF content",
        [sol["title"] for sol in st.session_state.last_results["solutions"]]
    )
    
    if selected_solution:
        solution = next(
            sol for sol in st.session_state.last_results["solutions"] 
            if sol["title"] == selected_solution
        )
        
        with st.spinner("Loading PDF content..."):
            recommender = SHLRecommender()
            pdf_text = recommender.get_pdf_content(solution["download_url"])
            
            st.subheader(f"Extracted Content from {solution['title']}")
            st.expander("View Full PDF Text").write(pdf_text)
            
            st.download_button(
                label="Download Original PDF",
                data=requests.get(solution["download_url"]).content,
                file_name=f"{solution['title']}.pdf",
                mime="application/pdf"
            )

show_pdf_viewer()