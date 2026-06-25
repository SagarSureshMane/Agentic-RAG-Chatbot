# Agentic RAG Chatbot

An Agentic AI-powered Retrieval-Augmented Generation (RAG) chatbot built using LangGraph, LangChain, OpenAI LLMs, ChromaDB, and Streamlit.

The application combines multiple tools with document retrieval capabilities, enabling users to interact with uploaded documents and external information sources through a single conversational interface.

## Features

### Agentic AI Workflow

* Built using LangGraph ReAct Agent
* Multi-tool reasoning and execution
* Dynamic tool selection based on user queries

### RAG (Retrieval-Augmented Generation)

* Upload and process PDF files
* Upload and process DOCX files
* Upload and process TXT files
* Upload and process Excel files
* Automatic document chunking and embedding generation
* Semantic search using vector database

### Integrated Tools

#### Web Search

* Real-time internet search using Tavily Search

#### Wikipedia Search

* Fetch information from Wikipedia

#### Calculator Tool

* Perform mathematical calculations

#### SQL Query Tool

* Query structured databases using natural language

#### PDF Reader

* Extract content from PDF documents

#### Excel Analyzer

* Analyze spreadsheet data

#### Email Tool

* Generate and send emails

## Tech Stack

### LLM & AI Frameworks

* LangChain
* LangGraph
* OpenAI / Groq

### Vector Database

* ChromaDB

### Frontend

* Streamlit

### Embedding Models

* OpenAI Embeddings

### Programming Language

* Python

## Project Architecture

User Query
↓
LangGraph Agent
↓
Tool Selection
├── Web Search
├── Wikipedia Search
├── Calculator
├── SQL Query
├── RAG Search
├── PDF Reader
├── Excel Analyzer
└── Email Tool
↓
LLM Response

## Folder Structure

Agentic_RAG_Chatbot/
│
├── app.py
├── agents/
│   └── graph.py
│
├── tools/
│   ├── calculator.py
│   ├── web_search.py
│   ├── wikipedia_tool.py
│   ├── rag_tool.py
│   ├── sql_tool.py
│   ├── pdf_tool.py
│   ├── excel_tool.py
│   └── email_tool.py
│
├── rag/
│   ├── ingest.py
│   ├── loaders.py
│   └── vector_store.py
│
├── chroma_db/
├── uploads/
├── requirements.txt
└── README.md

## Installation

### Clone Repository

git clone https://github.com/your-username/Agentic_RAG_Chatbot.git

cd Agentic_RAG_Chatbot

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:
venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_key

TAVILY_API_KEY=your_tavily_key

### Run Application

streamlit run app.py

## Future Improvements

* Multi-user chat sessions
* Conversation memory using PostgreSQL
* Hybrid Search (Keyword + Vector Search)
* Source citations
* LangSmith tracing
* Multi-agent architecture
* Reranking for better retrieval accuracy

## Learning Outcomes

This project demonstrates:

* Agentic AI Development
* LangGraph Workflow Design
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Tool Calling Agents
* LLM Integration
* Streamlit Application Development
* Document Intelligence Systems
