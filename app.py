import streamlit as st
from pipelines.router import route_query
from memory.chat_history import ChatHistory
from dotenv import load_dotenv

import tempfile
import os
from rag.ingest import ingest_pdf, ingest_text, ingest_web
from rag.vectorstore import clear_vectorstore

load_dotenv()

# --------------------------------------------------
# Page config
# --------------------------------------------------

st.set_page_config(
    page_title="Chatbot",
    layout="centered",
)

st.title("RETRIEVIST") 

# --------------------------------------------------
# Session State: Chat History
# --------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatHistory()

if "kb_initialized" not in st.session_state:
    st.session_state.kb_initialized = False

if not st.session_state.kb_initialized:
    clear_vectorstore()
    st.session_state.kb_initialized = True
    with st.sidebar:
        st.info("🧹 Knowledge base cleared for this session")


history: ChatHistory = st.session_state.chat_history

# --------------------------------------------------
# Display chat history
# --------------------------------------------------

for msg in history.get_messages():
    if msg.type == "human":
        st.chat_message("user").write(msg.content)
    elif msg.type == "ai":
        st.chat_message("assistant").write(msg.content)


# --------------------------------------------------
# User input
# --------------------------------------------------

user_input = st.chat_input("Ask something...")

if user_input:
    st.chat_message("user").write(user_input)
    history.add_user_message(user_input)

    with st.spinner("Thinking..."):
        response = route_query(user_input, history)

    st.chat_message("assistant").write(response)
    history.add_ai_message(response)

# --------------------------------------------------
# Sidebar (Knowledge Base + Options)
# --------------------------------------------------

with st.sidebar:
    st.header("📚 Knowledge Base")

    # ===========================
    # PDF Upload
    # ===========================
    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
    add_pdf = st.button("Add PDF to Knowledge Base")

    if add_pdf:
        if not uploaded_pdf:
            st.error("Please upload a PDF file.")
        else:
            with st.spinner("Processing PDF..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_pdf.read())
                    tmp_path = tmp.name

                chunks = ingest_pdf(tmp_path)
                os.remove(tmp_path)

            st.success(f"PDF ingested successfully ({chunks} chunks).")

    st.markdown("---")

    # ===========================
    # Text File Upload
    # ===========================
    uploaded_text = st.file_uploader("Upload Text File", type=["txt"])
    add_text = st.button("Add Text to Knowledge Base")

    if add_text:
        if not uploaded_text:
            st.error("Please upload a text file.")
        else:
            with st.spinner("Processing text file..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
                    tmp.write(uploaded_text.read().decode("utf-8", errors="ignore").encode("utf-8"))
                    tmp_path = tmp.name

                chunks = ingest_text(tmp_path)
                os.remove(tmp_path)

            st.success(f"Text file ingested successfully ({chunks} chunks).")

    st.markdown("---")

    # ===========================
    # Web URL
    # ===========================
    web_url = st.text_input("Enter Web URL")
    add_web = st.button("Add Web Page to Knowledge Base")

    if add_web:
        if not web_url:
            st.error("Please enter a valid URL.")
        else:
            with st.spinner("Fetching and processing web page..."):
                chunks = ingest_web(web_url)

            st.success(f"Web page ingested successfully ({chunks} chunks).")

    st.markdown("---")

    # ===========================
    # Options
    # ===========================
    st.header("⚙️ Options")

    if st.button("Clear chat history"):
        history.clear()
        st.rerun()

    if st.button("🧹 Clear Knowledge Base"):
        with st.spinner("Clearing knowledge base..."):
            clear_vectorstore()
        st.session_state.kb_initialized = True
        st.success("Knowledge base cleared successfully.")


    st.markdown("---")
    st.markdown("**Architecture**")
    st.markdown(
        """
        - RAG (Pinecone)
        - Tools (Wikipedia, ArXiv, Calculator)
        - Router-based control
        - In-memory chat history
        """
    )

