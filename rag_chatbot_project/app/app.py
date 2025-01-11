import streamlit as st
from data_loader import load_data
from rag_pipeline import setup_rag_pipeline
from chatbot import chatbot_response

st.title("RAG-Based Chatbot")

#data
data_file = r"C:\Users\ayush\buildfast\rag_chatbot_project\data\sample_data.csv"  # Ensure this file exists at the specified path
data = load_data(data_file)

# rag_pipe
pipeline = setup_rag_pipeline(data)

#ask the chatbot
st.subheader("Ask the Chatbot")
user_query = st.text_input("Enter your question:")
if user_query:
    response = chatbot_response(user_query, pipeline)
    st.write(f"Chatbot: {response}")
