import os

# Define the directory structure
directory_structure = {
    "shl-recommender": {
        ".gitignore": "",
        "README.md": "# SHL Recommender\nThis is the SHL Recommender application.",
        "requirements.txt": "streamlit\npandas\nnumpy\nrequests\nchroma",
        "app.py": """import streamlit as st
import components.header as header
import components.sidebar as sidebar
import pages.1_🏠_Home as home

def main():
    header.show_header()
    sidebar.show_sidebar()
    home.show_home()

if __name__ == "__main__":
    main()""",
        "config.py": """# Configuration settings for SHL Recommender
API_KEY = "your-api-key-here"
DATABASE_URL = "your-database-url-here" """,
        "assets": {
            "style.css": "/* Custom styles for SHL Recommender */\nbody { font-family: Arial, sans-serif; }",
            "shl-logo.png": ""  # You can add a sample logo or leave it as empty
        },
        "components": {
            "header.py": """import streamlit as st

def show_header():
    st.title("SHL Recommender")
    st.subheader("Personalized recommendations for you")""",
            "sidebar.py": """import streamlit as st

def show_sidebar():
    st.sidebar.header("Navigation")
    st.sidebar.selectbox("Choose a page", ["Home", "Search", "Feedback"])""",
            "feedback.py": """import streamlit as st

def show_feedback():
    st.header("Feedback")
    st.text_area("Your feedback:")
    st.button("Submit Feedback")"""
        },
        "services": {
            "recommender.py": """class Recommender:
    def __init__(self):
        pass

    def get_recommendations(self, user_input):
        # Add recommendation logic here
        return ["Recommendation 1", "Recommendation 2", "Recommendation 3"]""",
            "pdf_processor.py": """class PDFProcessor:
    def __init__(self):
        pass

    def process_pdf(self, file_path):
        # Add PDF processing logic here
        return "Processed PDF content" """,
            "chroma_manager.py": """class ChromaManager:
    def __init__(self):
        pass

    def save_data(self, data):
        # Add logic for saving data to ChromaDB
        pass"""
        },
        "pages": {
            "1_🏠_Home.py": """import streamlit as st

def show_home():
    st.header("Welcome to SHL Recommender")
    st.write("This is the home page of the SHL Recommender.")""",
            "2_🔍_Search.py": """import streamlit as st

def show_search():
    st.header("Search Recommendations")
    query = st.text_input("Enter your search query:")
    if query:
        st.write(f"Searching for {query}...")""",
            "3_📊_Feedback.py": """import streamlit as st

def show_feedback():
    st.header("Feedback Analysis")
    st.write("This page shows feedback analysis.")"""
        }
    }
}

# Function to create the directory structure
def create_directory_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_directory_structure(path, value)
        else:
            # Use UTF-8 encoding to avoid UnicodeEncodeError
            with open(path, "w", encoding="utf-8") as file:
                file.write(value)

# Create the base directory and structure
base_dir = "shl-recommender"
os.makedirs(base_dir, exist_ok=True)
create_directory_structure(base_dir, directory_structure)
print("Directory structure created successfully!")
