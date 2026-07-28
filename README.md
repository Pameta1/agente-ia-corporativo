# Asistente de Conocimiento Corporativo (RAG) - Tienda Dany 🌸

Aplicación basada en Inteligencia Artificial y la arquitectura RAG (Retrieval-Augmented Generation) diseñada específicamente para responder consultas sobre normativas, políticas, FAQs y el catálogo de productos de la tienda artesanal de Dany. Esta plataforma centraliza la atención al cliente para prendas y accesorios únicos pintados a mano (chaquetas de mezclilla, gorros y bolsas con diseños florales y de colibríes).

---

## 🚀 Problemática y Solución

### Problemática
* **Gestión de consultas frecuentes:** Los clientes suelen requerir información detallada y rápida sobre tiempos de envío, políticas de devolución, plazos de entrega y características de los productos artesanales.
* **Sobrecarga operativa:** Responder de forma manual a cada consulta repetitiva en los canales de venta resta tiempo para la creación artística y la producción de nuevas piezas.
* **Dispersión de la información:** Las políticas de la tienda y los detalles de los productos se encontraban desorganizados, dificultando una respuesta unificada y coherente.

### Solución Implementada
* **Asistente Conversacional RAG:** Un agente inteligente entrenado con la documentación oficial de la tienda (políticas, términos, FAQs y guías) que procesa preguntas en lenguaje natural.
* **Búsqueda Semántica:** Capacidad para comprender la intención del usuario más allá de las palabras exactas utilizadas gracias a la indexación vectorial.
* **Trazabilidad Transparente:** El sistema muestra de forma clara los fragmentos documentales de origen utilizados para redactar cada respuesta, evitando alucinaciones de la IA.
* **Despliegue en la Nube:** Interfaz web ligera, accesible y conectada de forma continua a través de Streamlit Cloud.

---

## 🛠️ Arquitectura de la Solución y Flujo RAG

El flujo técnico implementado en el sistema sigue las etapas estándar de un pipeline RAG moderno:

1. **Ingesta y Procesamiento de Documentos:** Carga de archivos de políticas, normativas y preguntas frecuentes de la tienda.
2. **Chunking (Fragmentación):** División de los textos corporativos en bloques manejables para mantener la precisión semántica.
3. **Indexación Vectorial:** Transformación de los fragmentos en representaciones numéricas mediante embeddings para su almacenamiento y búsqueda rápida.
4. **Capa de Recuperación (Retrieval):** Ante la pregunta del usuario, el sistema transforma la consulta en vector y busca los fragmentos más cercanos semánticamente.
5. **Generación con LLM:** Se construye un prompt contextualizado que alimenta al modelo de lenguaje para redactar una respuesta precisa, incluyendo las fuentes de origen y un mecanismo de *fallback* si la información no está disponible.

---

## 📂 Librerías y Tecnologías Utilizadas

* **Python:** Lenguaje principal de programación y lógica del backend.
* **Streamlit:** Framework para el desarrollo y despliegue rápido de la interfaz gráfica web.
* **LangChain / LlamaIndex (o librerías de soporte RAG):** Orquestadores para la gestión de fragmentos, vectores y llamadas al LLM.
* **Git y GitHub:** Control de versiones y almacenamiento del código fuente corporativo.
* **Streamlit Community Cloud:** Plataforma de alojamiento en la nube para la ejecución pública de la aplicación.
---

## 🗂️ Estructura del Proyecto

```text
agente-ia-corporativo/
│
├── data/               # Documentación base (Políticas, FAQs, Envíos, Términos)
├── app.py              # Script principal de la aplicación Streamlit
├── requirements.txt    # Dependencias y librerías del proyecto
└── README.md           # Documentación técnica y descriptiva del proyecto

---
🎯 Funciones y Accesos Rápidos
Barra de Consultas Inteligente: Campo de texto interactivo para plantear dudas sobre la tienda.

Visualización de Contexto RAG: Menú desplegable para revisar los fragmentos exactos de los documentos utilizados en la respuesta.

Respuestas Verificables: Enlaces a canales de soporte interno y políticas oficiales de la marca.

💡 Ejemplos de Preguntas para Probar el Deploy
Puedes probar las siguientes consultas directamente en la aplicación en línea para verificar su comportamiento:

"¿Cuál es el horario de atención al cliente?"

"¿Cómo puedo solicitar un reembolso o cambio para una compra online?"

"¿Cuáles son los plazos y condiciones para la entrega de los productos?"

"¿Cuál es la política de privacidad de la tienda?"

🧥 Muestra de Productos (Tienda Dany)
El taller de Dany se especializa en la creación de piezas únicas pintadas a mano, destacando chaquetas de mezclilla, gorros y bolsas personalizadas con motivos florales y de naturaleza:

Chaquetas de Mezclilla: Diseños exclusivos de colibríes y flores silvestres pintados artesanalmente.

Accesorios: Gorros y bolsas de tela adaptados con detalles botánicos únicos.

 ## 🌐 Demo en línea

🔗 [Ver demo en línea](https://agente-ia-corporativo-m9zyfcnx6uju2wkshb6fyu.streamlit.app/)


## 📸 Demostración del Agente en la Nube
Vista General de la Interfaz
Funcionamiento y Respuestas del RAG
Vista General de la Interfaz
Funcionamiento y Respuestas del RAG
### Vista General de la Interfaz
![Interfaz de la aplicación](https://github.com/deploy-1.png)

### Funcionamiento y Respuestas del RAG
![Resultados del Agente](https://github.com/deploy-2.png)
