from data_loader import load_all_documents
from embedding import EmbeddingPipeline
from vectorstore import FaissVectorStore
from search import RAGSearch


if __name__ == "__main__":
    # documents = load_all_documents("../data")
    # print(f"Chunking and embedding {len(documents)} documents...")
    store=FaissVectorStore("faiss_store")
    store.load()    
    # print(store.query("What are the Related literature?", top_k=3))
    # store.build_from_documents(documents)


    rag_search = RAGSearch()
    query = "Who uses Agentic AI?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
