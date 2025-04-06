import streamlit as st
import pandas as pd

def show_feedback_analytics():
    st.title("📊 Feedback Analytics")
    
    # In production, this would come from a database
    sample_data = {
        "Date": ["2025-04-06", "2023-04-06", "2025-04-06"],
        "Rating": ["Yes", "No", "Yes"],
        "Comments": ["Great!", "Not relevant", "Helpful"],
        "Solution": ["Data Entry Test", "Leadership Assessment", "HR Entry Test"]
    }
    
    df = pd.DataFrame(sample_data)
    
    st.subheader("Recent Feedback")
    st.dataframe(df)
    
    st.subheader("Feedback Distribution")
    rating_counts = df["Rating"].value_counts()
    st.bar_chart(rating_counts)
