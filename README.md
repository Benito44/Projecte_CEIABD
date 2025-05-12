# 🧠 Intel·ligència Artificial i Processament del Llenguatge Natural

## 📚 Models de llenguatge i embeddings

- Ús de `SentenceTransformer` amb el model `all-MiniLM-L6-v2` per generar vectors semàntics del contingut textual.
- Càlcul de similitud semàntica mitjançant:
  - `cosine_similarity` de `sklearn.metrics.pairwise`.
  - `util.cos_sim` de `sentence_transformers.util`.

## 🧠 Processament del llenguatge amb spaCy

- Anàlisi lingüística usant el model `es_core_news_sm` per a:
  - **Lematització**.
  - **Filtrat de paraules clau**, conservant:
    - Substantius
    - Noms propis
    - Verbs
    - Adjectius

# 🔍 Cerca Semàntica

- Combinació de dues estratègies:
  - `knn` sobre embeddings per cercar per significat.
  - `match` per a coincidència textual tradicional.
- Extracció del **fragment més rellevant** basat en la similitud entre fragments del document i la consulta de lusuari.

# 🗃️ Big Data i Tecnologies d'Emmagatzematge / Indexació



## &#9729;&#65039; Azure Blob Storage 

- Càrrega i descàrrega d'arxius des de contenidors [al | en el] núvol.
- Ús de: 
- ** Metadades personalitzades** 
- ** Generació d'URLs SAS** (Shared Access Signature) per compartir [arxius | arxivaments] de forma segura. 

## &#128230; Elasticsearch (Cloud) 

- Creació d'un índex ** vectorial híbrid** amb: 
- [Camps | Campos] 'donin-se_vector' per a *embeddings semàntics.
- [Camps | Campos] 'text', '*keyword', '[dona't | dati]' per a [cerques | recerques] estructurades.
- Configuració d'un ** *analyzer personalitzat** amb eliminació d'accents (ideal per a textos en espanyol). 

## &#128209; Documents processats 

| Format | Eines utilitzades | 
|---------|--------------------------------------------------| 
| '.docx' | '*python-*docx', 'docx.core_properties' | 
| <ABPQOPSTTUR>.pdf' | '*pdfplumber', 'PyPDF2' ('*pypdf') | 
| '.xls' | '*olefile' per a extracció de metadades | 

## &#128200; Emmagatzemament estructurat (Parquet) 

- Conversió de resultats a 'DataFrame' amb '[colles | pandes]'.
- [Guardat | Guardado] com a [arxiu | arxivament] '.parquet' (format columnar optimitzat).
- [Pujada | Puja | Ascensió | Pujament] [de l'arxiu | de l'arxivament] final a ** Azure Blob Storage** amb estructura de carpetes organitzades per ** data**. 

# &#129513; Funcionalidades [Clave | Clau | Clavi] del Sistema 

| Funcionalitat | Tecnologia utilitzada | 
|--------------------------------------|--------------------------------------------| 
| Generació de *embeddings semàntics | 'SentenceTransformer' | 
| Processament de paraules clau NLP | '*spaCy' ('és_Core_news_sm') | 
| [Cerca | Recerca] semàntica i textual | 'Elasticsearch' (*cloud, vector + matx) | 
| [Estoc | Emmagatzematge] [d'arxius | d'arxivaments]/resultats| Azure Blob Storage, format '.parquet' | 
| Extracció de text de documents | '*python-*docx', '*pdfplumber', '*pypdf', '*openpyxl' | 
| Extracció de metadades de documents| 'docx.core_properties', '*olefile', metadades d'Azure Blob | 
