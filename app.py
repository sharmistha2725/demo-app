import streamlit as st
import openai
from PIL import Image

# Streamlit UI Setup
st.set_page_config(page_title="EduGenius AI", layout="wide")

# Title & Description
st.title("Personalized AI Tutor")
st.write("An AI-powered tutor that provides **instant explanations, auto-corrects assignments, and adapts to your learning style.**")

# Sidebar Menu
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to", ["Ask a Question", "Upload Assignment", "Learning Dashboard"])

# Section: Ask a Question
if menu == "Ask a Question":
    st.subheader("Question")
    user_question = st.text_area("Tye your question")

    if st.button("Get Answer"):
        if user_question:
            st.success("AI Answer: This is where the LLM-generated response will appear.")
        else:
            st.warning("Please enter a question.")

    # Voice Input (Placeholder)
    st.write("**Voice Input**")

# Section: Upload Assignment
elif menu == "Upload Assignment":
    st.subheader("Upload Your Assignment")
    uploaded_file = st.file_uploader("Upload a handwritten or typed document for auto-correction.", type=["png", "jpg", "jpeg", "pdf"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Assignment", use_column_width=True)
        st.success("Your assignment has been uploaded.")

# Section: Learning Dashboard
elif menu == "Learning Dashboard":
    st.subheader(" Your Learning Progress")
    st.write("Feature Coming Soon: Track your learning progress, completed topics, and AI recommendations!")