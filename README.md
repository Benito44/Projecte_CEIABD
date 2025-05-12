
![Analisis de Documents ](https://github.com/user-attachments/assets/68570cc1-3d4d-488c-864e-c8a9791ebfc1)


# 🧠 Inteligencia Artificial y Procesamiento del Lenguaje Natural

## 📚 Modelos de lenguaje y embeddings

- Uso de `SentenceTransformer` con el modelo `all-MiniLM-L6-v2` para generar vectores semánticos del contenido textual.
- Cálculo de similitud semántica mediante:
  - `cosine_similarity` de `sklearn.metrics.pairwise`.
  - `util.cos_sim` de `sentence_transformers.util`.

## 🧠 Procesamiento del lenguaje con spaCy

- Análisis lingüístico usando el modelo `es_core_news_sm` para:
  - **Lematización**.
  - **Filtrado de palabras clave**, conservando:
    - Sustantivos
    - Nombres propios
    - Verbos
    - Adjetivos

# 🔍 Búsqueda Semántica

- Combinación de dos estrategias:
  - `knn` sobre embeddings para búsqueda por significado.
  - `match` para coincidencia textual tradicional.
- Extracción del **fragmento más relevante** basado en la similitud entre fragmentos del documento y la consulta del usuario.

# 🗃️ Big Data y Tecnologías de Almacenamiento / Indexación

## ☁️ Azure Blob Storage

- Carga y descarga de archivos desde contenedores en la nube.
- Uso de:
  - **Metadatos personalizados**
  - **Generación de URLs SAS** (Shared Access Signature) para compartir archivos de forma segura.

## 📦 Elasticsearch (Cloud)

- Creación de un índice **vectorial híbrido** con:
  - Campos `dense_vector` para embeddings semánticos.
  - Campos `text`, `keyword`, `date` para búsquedas estructuradas.
- Configuración de un **analyzer personalizado** con eliminación de acentos (ideal para textos en español).

## 📑 Documentos procesados

| Formato | Herramientas utilizadas                          |
|---------|--------------------------------------------------|
| `.docx` | `python-docx`, `docx.core_properties`            |
| `.pdf`  | `pdfplumber`, `PyPDF2` (`pypdf`)                 |
| `.xls`  | `olefile` para extracción de metadatos           |

## 📈 Almacenamiento estructurado (Parquet)

- Conversión de resultados a `DataFrame` con `pandas`.
- Guardado como archivo `.parquet` (formato columnar optimizado).
- Subida del archivo final a **Azure Blob Storage** con estructura de carpetas organizadas por **fecha**.

# 🧩 Funcionalidades Clave del Sistema

| Funcionalidad                         | Tecnología utilizada                       |
|--------------------------------------|--------------------------------------------|
| Generación de embeddings semánticos  | `SentenceTransformer`                      |
| Procesamiento de palabras clave NLP  | `spaCy` (`es_core_news_sm`)                |
| Búsqueda semántica y textual         | `Elasticsearch` (cloud, vector + match)    |
| Almacenamiento de archivos/resultados| Azure Blob Storage, formato `.parquet`     |
| Extracción de texto de documentos    | `python-docx`, `pdfplumber`, `pypdf`, `openpyxl` |
| Extracción de metadatos de documentos| `docx.core_properties`, `olefile`, metadatos de Azure Blob |

