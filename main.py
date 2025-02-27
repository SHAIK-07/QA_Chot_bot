import streamlit as st
from helper import get_qa_chain, create_vector_db

# Page Configuration
st.set_page_config(page_title="Codebasics Q&A", page_icon="🌱", layout="wide")

# Sidebar: Create Knowledgebase
st.sidebar.header("Knowledgebase Settings")
st.sidebar.markdown("Create a knowledgebase to power the chatbot.")
if st.sidebar.button("1st click me!"):
    with st.spinner("Creating vector database... ⏳"):
        create_vector_db()
    st.sidebar.success("Knowledgebase created! ✅")

# Title
st.title("💬 Codebasics Q&A Chatbot")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input
question = st.text_input("Ask me anything related to Codebasics:")

if question:
    # Load chain only once
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = get_qa_chain()
    
    with st.spinner("Thinking... 🤔"):
        response = st.session_state.qa_chain.invoke({"query": question})

    # Store conversation history
    st.session_state.chat_history.append((question, response["result"]))

# Display Chat History
if st.session_state.chat_history:
    st.subheader("Chat History")
    for q, a in st.session_state.chat_history[::-1]:  # Show latest first
        with st.chat_message("user"):
            st.write(f"**Q:** {q}")
        with st.chat_message("assistant"):
            st.write(f"**A:** {a}")
