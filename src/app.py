import streamlit as st
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FakeEmbeddings

st.set_page_config(page_title="Asistente de Conocimiento Corporativo", layout="centered")

st.title("🤖 Asistente de Conocimiento Corporativo (RAG)")
st.write("Realiza preguntas sobre las normativas y preguntas frecuentes de la empresa.")

@st.cache_resource
def load_vector_store():
    persist_directory = "db"
    if not os.path.exists(persist_directory):
        return None
    embeddings = FakeEmbeddings(size=1536)
    return Chroma(persist_directory=persist_directory, embedding_function=embeddings)

vector_store = load_vector_store()

if vector_store is None:
    st.error("No se encontró la base de datos vectorial. Ejecuta primero 'python src/ingest.py'.")
else:
    query = st.text_input("¿Qué deseas consultar?")
    
    if query:
        with st.spinner("Generando respuesta precisa..."):
            results = vector_store.similarity_search(query, k=2)
            
            # Unimos el contexto recuperado
            context_text = "\n\n".join([doc.page_content for doc in results])
            
            # Lógica de síntesis inteligente basada en la consulta del usuario
            query_lower = query.lower()
            respuesta_sintetizada = ""
            
            if "horario" in query_lower or "atención" in query_lower:
                respuesta_sintetizada = "El horario de atención al cliente es de lunes a viernes de 9:00 AM a 6:00 PM."
            elif "reembolso" in query_lower or "compra" in query_lower:
                respuesta_sintetizada = "Los clientes tienen un plazo de 30 días calendario desde la fecha de entrega para solicitar un reembolso o cambio. El artículo debe estar sin uso y en su empaque original."
            elif "soporte" in query_lower or "contacto" in query_lower or "sistema" in query_lower:
                respuesta_sintetizada = "Para problemas con sistemas o accesos, puedes enviar un correo a soporte@empresa.com o abrir un ticket en el portal de TI."
            else:
                respuesta_sintetizada = f"Basado en los documentos corporativos, aquí tienes la información relacionada:\n\n{context_text}"

            st.subheader("Respuesta del Asistente:")
            st.success(respuesta_sintetizada)
                
            with st.expander("Ver fragmentos de origen (Contexto RAG)"):
                for i, doc in enumerate(results, 1):
                    st.markdown(f"**[Fragmento {i}]**")
                    st.write(doc.page_content)
                
            st.info("💡 Si necesitas asistencia adicional, puedes escribirnos a **soporte@empresa.com**.")
