import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FakeEmbeddings

def query_vector_db():
    persist_directory = "db"
    
    if not os.path.exists(persist_directory):
        print("No se encontró la base de datos vectorial. Ejecuta primero ingest.py.")
        return

    embeddings = FakeEmbeddings(size=1536)
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    
    query = "¿Cuál es la política de reembolsos?"
    print(f"Consulta: '{query}'\n")
    
    results = vector_store.similarity_search(query, k=2)
    
    print("--- Fragmentos recuperados ---")
    for i, doc in enumerate(results, 1):
        print(f"\n[Resultado {i}]")
        print(doc.page_content)

if __name__ == "__main__":
    query_vector_db()
