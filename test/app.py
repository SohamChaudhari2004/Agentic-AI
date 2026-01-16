import os
from dotenv import load_dotenv
load_dotenv()

# LLM
from groq import Groq

# LangChain pieces
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings  # Fixed import
from langchain.schema import Document
from langchain_groq import ChatGroq  # Better integration with LangChain

# initialize Groq LLM
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class ModularRAG:
    def __init__(self, llm_model="openai/gpt-oss-20b"):  # Use valid Groq model name
        # Initialize LLM using LangChain's ChatGroq wrapper (better for chains)
        self.llm = ChatGroq(
            groq_api_key=os.environ.get("GROQ_API_KEY"),
            model_name=llm_model,
            temperature=0
        )
        self.modules = {}  # Store module_name -> retriever mapping

    def register_module(self, module_name, retriever):
        """
        Register a module with its retriever.
        Example: rag_system.register_module("literature", retriever_obj)
        """
        self.modules[module_name] = retriever

    def query(self, user_query, target_modules=None, top_k=5):
        """
        Run a query against one or more modules.

        Args:
            user_query (str): The input query.
            target_modules (list[str] | None): If None, search all modules.
            top_k (int): Number of documents to retrieve.
        """
        results = {}

        # Select modules (all if not specified)
        selected_modules = target_modules or self.modules.keys()

        for module_name in selected_modules:
            retriever = self.modules[module_name]

            # Make sure the retriever uses the requested top_k
            if hasattr(retriever, "search_kwargs"):
                retriever.search_kwargs = {"k": top_k}

            # Build a chain for this module
            chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=True,
            )

            # Run the query
            response = chain({"query": user_query})
            results[module_name] = {
                "answer": response["result"],
                "sources": response["source_documents"],
            }

        return results

# -----------------------
# Chroma (chromadb) setup
# -----------------------

# Fixed embedding import
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_or_load_chroma_collection(collection_name, docs=None, persist_dir=None):
    """
    Create a Chroma collection from documents or load existing persisted collection.
    """
    persist_dir = persist_dir or f"./chroma_{collection_name}"
    if docs:
        # create (and persist) collection from documents
        vect = Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=persist_dir,
            collection_name=collection_name,
        )
    else:
        # load existing persisted collection
        vect = Chroma(
            persist_directory=persist_dir,
            embedding_function=embeddings,
            collection_name=collection_name,
        )
    # return a Retriever
    return vect.as_retriever()

# Example documents
example_docs_lit = [
    Document(page_content="RAG combines retrieval with a generative model to provide contextually relevant responses.", metadata={"source": "paper1"}),
    Document(page_content="Retrieval pipelines usually include indexing and vector search for finding relevant documents.", metadata={"source": "blog1"}),
]
example_docs_preproc = [
    Document(page_content="We normalized images with mean/std and applied data augmentation techniques.", metadata={"source": "exp_notes"}),
]
example_docs_results = [
    Document(page_content="Results: accuracy reached 92% on dataset X with improved preprocessing pipeline.", metadata={"source": "results_table"}),
]

# Create or load chroma-backed retrievers for modules
literature_retriever = create_or_load_chroma_collection("literature", docs=example_docs_lit)
preproc_retriever = create_or_load_chroma_collection("preprocessing", docs=example_docs_preproc)
results_retriever = create_or_load_chroma_collection("results", docs=example_docs_results)

# -----------------------
# Initialize system
# -----------------------
rag_system = ModularRAG(llm_model="openai/gpt-oss-20b")  # Use valid Groq model

# Register modules with retrievers
rag_system.register_module("literature", literature_retriever)
rag_system.register_module("preprocessing", preproc_retriever)
rag_system.register_module("results", results_retriever)

# Query a single module
response = rag_system.query("Summarize RAG approaches for ML pipelines", target_modules=["literature"])
print("Literature Response:", response["literature"]["answer"])

# Query across ALL modules
multi_response = rag_system.query("What datasets and preprocessing were used in experiments?")
for module, result in multi_response.items():
    print(f"\n[{module.upper()}]")
    print("Answer:", result["answer"])
    print("Sources:", [doc.metadata for doc in result["sources"]])