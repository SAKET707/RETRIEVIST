# 🔍 RETRIEVIST

**RETRIEVIST** is a modular, tool-augmented **RAG (Retrieval-Augmented Generation) chatbot** built with **Streamlit, LangChain, Groq LLMs, and Pinecone**.  
It intelligently routes user queries between **direct LLM reasoning**, **external tools**, and **document-based retrieval**, ensuring **accuracy over hallucination**.

## 🌐 **Live Demo:**  
👉 https://retrievist-by-saket.streamlit.app/

---

## ✨ Key Features

- 📚 **Retrieval-Augmented Generation (RAG)**
  - PDF, text, and web-page ingestion
  - Semantic search powered by Pinecone
- 🧠 **Router-based intelligence**
  - Automatically decides between:
    - General LLM response
    - Tool-enabled agent
    - RAG pipeline
- 🛠️ **Tool-enabled agent**
  - Wikipedia search
  - arXiv research paper lookup
  - Secure mathematical expression evaluation
- 🔐 **No hallucinations by design**
  - Uses tools only when required
  - Responds *"I don't know"* when information is unavailable
- ☁️ **Cloud deployed**
  - Hosted on Streamlit Community Cloud
  - Secrets managed securely 

---

## 🎬 Demo Walkthrough

<!-- Demo Screenshots -->
<div align="center">

  <!-- Row 1: 3 images -->
  <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 20px;">
    <img src="https://github.com/user-attachments/assets/768d5fcc-adcc-4916-99b6-cf41b5e36db1" alt="RETRIEVIST Demo 1" width="300">
    <img src="https://github.com/user-attachments/assets/3561679e-e83c-402f-a2e2-0e1da20beffa" alt="RETRIEVIST Demo 2" width="300">
    <img src="https://github.com/user-attachments/assets/8ffcb2d0-17fc-4230-a94a-f7a92248155e" alt="RETRIEVIST Demo 3" width="300">
  </div>

  <!-- Row 2: 2 images -->
  <div style="display: flex; justify-content: center; gap: 20px;">
    <img src="https://github.com/user-attachments/assets/739edd99-8ee9-4aae-a05f-2e8858f0c926" alt="RETRIEVIST Demo 4" width="300">
    <img src="https://github.com/user-attachments/assets/84884d64-4936-41ba-be61-0530c10c776c" alt="RETRIEVIST Demo 5" width="300">
  </div>

</div>

In the live demo, **RETRIEVIST** is exercised across multiple real-world scenarios to demonstrate its routing, retrieval, and tool-usage capabilities.

One of the demonstrations uses a news article from *India Today*:

🔗 *Over 2 lakh giving up Indian citizenship each year — what is behind the exodus to USA, UK, Canada, Australia explained*  
https://www.indiatoday.in/india/story/over-2-lakh-giving-up-indian-citizenship-each-year-what-is-behind-the-exodus-to-usa-uk-canada-australia-explained-why-2837119-2025-12-18

> **Credit & Attribution:**  
> All news articles referenced in this demo are published by **India Today**.  
> The original content, reporting, and editorial rights belong to their respective authors and **India Today**.  
> This project analyzes publicly available information strictly for educational and demonstration purposes.


---

### 🔍 What the demo showcases

- 🌐 **Web-based RAG**
  - Ingestion and questioning over a live news article (India Today)
- 📖 **Wikipedia tool usage**
  - Information lookup for publicly available topics such as *Elon Musk*  
  > No personal profiling, endorsement, or misrepresentation is intended
- 📄 **Research paper retrieval**
  - arXiv tool usage to explore findings from  
    *“Attention Is All You Need”*  
  > All academic credit and intellectual ownership remain with the original authors
- 📁 **Document ingestion**
  - User-provided `.txt` and `.pdf` files uploaded and queried
- 🧮 **Mathematical reasoning via tool execution**
  - Evaluation of expressions involving trigonometric, exponential, and logarithmic functions, e.g.:

```text
(3 * sin(pi / 4)**2 + 2 * cos(pi / 3)) * exp(1) + log(100) / sqrt(16)
```

---

## 🧩 Architecture Overview

RETRIEVIST follows a **clean, scalable, and extensible architecture** designed for clarity and future growth.

```text
RETRIEVIST/
├── app.py                  # Streamlit entry point
├── requirements.txt        # Python dependencies
├── .gitignore
│
├── config/                 # Centralized configuration
│   ├── settings.py         # Models, chunk sizes, Pinecone index
│   └── prompts.py          # System, RAG, Agent prompts
│
├── llms/                   # LLM & embedding abstractions
│   ├── groq_llm.py         # Groq LLM initialization
│   └── embeddings.py       # HuggingFace embeddings
│
├── rag/                    # Retrieval-Augmented Generation
│   ├── loaders.py          # PDF / text / web loaders
│   ├── splitter.py         # Document chunking logic
│   ├── vectorstore.py      # Pinecone integration
│   ├── ingest.py           # Knowledge base ingestion
│   └── rag_pipeline.py     # Core RAG logic
│
├── tools/                  # External tools for agents
│   ├── calculator.py       # Secure math evaluation
│   ├── wiki_tool.py        # Wikipedia search
│   └── arxiv_tool.py       # arXiv research lookup
│
├── pipelines/              # Query routing & execution
│   ├── router.py           # Decides: RAG vs Agent vs General
│   └── agent_pipeline.py   # Tool-enabled agent pipeline
│
├── memory/                 # Conversation memory
│   └── chat_history.py     # Session-based chat history
│
└── utils/                  # Helper utilities
    └── helpers.py          # Context formatting & text helpers

```

---
## 🔮 Future Improvements
Planned enhancements for upcoming iterations:
- Pinecone namespaces for multi-user isolation
- Source citations in RAG responses
- Smarter routing using intent classification
- Knowledge base analytics (document count, chunk stats)
- Role-based access control for ingestion
