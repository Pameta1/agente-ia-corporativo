import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import Chroma

def process_and_store_documents():
    file_path = os.path.join("data", "faq_empresa.txt")
    
    if not os.path.exists(file_path):
        print(f"No se encontró el archivo en {file_path}.")
        return

    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)
    
    # Usamos embeddings de prueba temporales para validar la arquitectura local
    embeddings = FakeEmbeddings(size=1536)
    
    # Guardamos los fragmentos en una base de datos Chroma local
    persist_directory = "db"
    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    print(f"¡Éxito! Se indexaron {len(docs)} fragmentos en la base de datos vectorial ChromaDB.")

if __name__ == "__main__":
    process_and_store_documents()
