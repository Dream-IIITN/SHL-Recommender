import streamlit as st

def collect_feedback():
    """Enhanced feedback collection component"""
    st.divider()
    st.markdown("### 💬 Help Us Improve")
    
    with st.form(key="feedback_form"):
        cols = st.columns(3)
        with cols[1]:
            rating = st.radio(
                "Was this helpful?",
                ["👍 Yes", "👎 No", "🤔 Partially"],
                horizontal=True,
                key="feedback_rating"
            )
        
        comments = st.text_area(
            "Additional comments (optional)",
            placeholder="What worked well or could be improved?",
            key="feedback_comments"
        )
        
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            # In a real app, you'd log this to a database
            st.session_state.feedback_submitted = True
            st.success("Thank you for your feedback! We'll use this to improve our recommendations.")
            
            # Print to console for demo purposes
            print(f"Feedback Received - Rating: {rating}, Comments: {comments}")