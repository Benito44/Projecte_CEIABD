

![Doc Analitic](https://github.com/user-attachments/assets/80a71f49-11e0-46aa-95b4-49949cc2a93a)



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
- Extracció del **fragment més rellevant** basat en la similitud entre fragments del document i la consulta de l’usuari.

# 🗃️ Big Data i Tecnologies d'Emmagatzematge / Indexació

## ☁️ Azure Blob Storage

- Càrrega i descàrrega d’arxius des de contenidors al núvol.
- Ús de:
  - **Metadades personalitzades**
  - **Generació d’URLs SAS** (Shared Access Signature) per compartir arxius de forma segura.

## 🗂️ Elasticsearch (Cloud)

- Creació d’un índex **vectorial híbrid** amb:
  - Camps `embedding_vector` per a *embeddings* semàntics.
  - Camps `text`, `keyword`, `data` per a cerques estructurades.
- Configuració d’un **analitzador personalitzat** amb eliminació d’accents (ideal per a textos en espanyol).

## 📄 Documents processats

| Format       | Eines utilitzades                                 |
|--------------|----------------------------------------------------|
| `.docx`      | `python-docx`, `docx.core_properties`              |
| `.pdf`       | `pdfplumber`, `PyPDF2` o `pypdf`                   |
| `.xls/.xlsx` | `olefile` per a metadades, `openpyxl` per a contingut |

## 📊 Emmagatzematge estructurat (Parquet)

- Conversió de resultats a `DataFrame` amb `pandas`.
- Guardat com a arxiu `.parquet` (format columnar optimitzat).
- Pujada de l’arxiu final a **Azure Blob Storage**, amb estructura de carpetes organitzades per **data**.

# 🧩 Funcionalitats Clau del Sistema

| Funcionalitat                      | Tecnologia utilitzada                        |
|-----------------------------------|----------------------------------------------|
| Generació d’embeddings semàntics  | `SentenceTransformer`                        |
| Processament de paraules clau NLP | `spaCy` (`es_core_news_sm`)                  |
| Cerca semàntica i textual         | `Elasticsearch` (cloud, vector + match)      |
| Emmagatzematge d’arxius/resultats | Azure Blob Storage, format `.parquet`        |
| Extracció de text de documents     | `python-docx`, `pdfplumber`, `pypdf`, `openpyxl` |
| Extracció de metadades             | `docx.core_properties`, metadades d’Azure Blob |

