import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import tempfile

# --------------------------
# Load environment variable
# --------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=api_key)

# --------------------------
# Streamlit page config
# --------------------------
st.set_page_config(page_title="📘 Gemini Notes & Questions Extractor", layout="wide")
st.title("🧠📄 Gemini PDF Notes & Question Generator (ChromaDB + SentenceTransformer)")

# --------------------------
# Upload the PDF
# --------------------------
uploaded_file = st.file_uploader("Upload your study or research PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("✅ PDF uploaded successfully! Extracting notes & questions...")

    # --------------------------
    # Load and split PDF
    # --------------------------
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    splitted_docs = text_splitter.split_documents(docs)

    # --------------------------
    # Initialize SentenceTransformer
    # --------------------------
    try:
        # Try to load the model (will use cache if available)
        embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    except Exception as e:
        st.error(f"Could not load embedding model. Error: {str(e)}")
        st.info("💡 Please ensure you have internet connection for the first run to download the model, or the model is already cached.")
        st.stop()

    # --------------------------
    # Compute embeddings
    # --------------------------
    embeddings = [embedding_model.encode(doc.page_content).tolist() for doc in splitted_docs]

    # --------------------------
    # ChromaDB setup
    # --------------------------
    collection_name = "notes_chunks"
    client = chromadb.Client(Settings(
        persist_directory="./chroma_notes",
        anonymized_telemetry=False
    ))

    # Delete collection if it exists and recreate
    try:
        client.delete_collection(name=collection_name)
    except:
        pass
    
    collection = client.create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )

    # Add documents to ChromaDB
    ids = [str(i) for i in range(len(splitted_docs))]
    texts = [doc.page_content for doc in splitted_docs]
    
    collection.add(
        embeddings=embeddings,
        documents=texts,
        ids=ids
    )

    # --------------------------
    # Gemini Model Setup
    # --------------------------
    model = genai.GenerativeModel("gemini-2.5-flash")

    # --------------------------
    # Generate Important Notes
    # --------------------------
    st.subheader("📝 Generate Notes")
    if st.button("Extract Key Notes"):
        all_text = "\n".join([doc.page_content for doc in splitted_docs])
        prompt_notes = f"""
You are a professional note summarizer.

Extract the *most important concepts, facts, definitions, and points* from the following PDF content.

Keep the summary structured, clear, and concise using bullet points or short sections.

PDF Content:
{all_text[:10000]}  # Limit large inputs
"""
        response_notes = model.generate_content(prompt_notes)
        st.markdown("### 📋 Key Notes:")
        st.write(response_notes.text)

    # --------------------------
    # Generate Practice Questions
    # --------------------------
    st.subheader("❓ Generate Practice / Viva Questions")
    if st.button("Generate Questions"):
        all_text = "\n".join([doc.page_content for doc in splitted_docs])
        prompt_questions = f"""
You are an educator.

Based on the following study material, generate *thought-provoking questions* that test conceptual understanding.

Include:
- 5 Easy Questions
- 5 Medium Questions
- 5 Advanced or Application-based Questions

Keep them relevant and academic.

PDF Content:
{all_text[:10000]}  # Limit large inputs
"""
        response_questions = model.generate_content(prompt_questions)
        st.markdown("### 🧩 Practice Questions:")
        st.write(response_questions.text)

    # --------------------------
    # Optional: Ask custom question
    # --------------------------
    st.subheader("💬 Ask a Custom Question from PDF")
    user_query = st.text_input("Type your question here:")
    if user_query:
        user_embedding = embedding_model.encode(user_query).tolist()
        search_results = collection.query(
            query_embeddings=[user_embedding],
            n_results=3
        )
        matched_texts = search_results['documents'][0]
        joined_text = "\n---\n".join(matched_texts)

        system_prompt = f"""
The user uploaded a PDF and asked a question.

Relevant content:
{joined_text}

User Question:
{user_query}

Now answer clearly, with explanations or examples.
"""
        chat_model = model.start_chat()
        response = chat_model.send_message(system_prompt)
        st.markdown("### 🤖 Gemini's Answer:")
        st.write(response.text)