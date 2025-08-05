# 🧠 LLM-Powered Personal Research Assistant

This is a Streamlit-based research assistant that helps you quickly analyze PDFs or web articles using the power of Retrieval-Augmented Generation (RAG) and large language models like OpenAI's GPT-4o.

The app allows you to:
- Upload a PDF or enter a URL
- Generate an executive summary
- Ask your own questions about the content
- Get follow-up reading suggestions

Built using modern LLM and vector search pipelines. Deployable on Streamlit Cloud.

---

## 🚀 Features

- ✅ Upload and parse **PDF files**
- ✅ Scrape article content from **URLs** using `requests` + `BeautifulSoup`
- ✅ Chunk text intelligently for embedding
- ✅ Embed and store vectors using **FAISS**
- ✅ Semantic Q&A via **GPT-4o**
- ✅ Executive summaries + follow-up reading suggestions
- ✅ Fully compatible with **Streamlit Cloud**

---

## 🧰 Tech Stack

| Component        | Tool                        |
|------------------|-----------------------------|
| UI               | Streamlit                   |
| LLM              | OpenAI GPT-4o               |
| Embedding Model  | OpenAI `text-embedding-3-small` |
| Vector Search    | FAISS                       |
| PDF Parsing      | PyMuPDF                     |
| Web Scraping     | Requests + BeautifulSoup    |
| Secrets Mgmt     | `python-dotenv`             |

---

## 📦 Installation

```bash
git clone https://github.com/joeldhamilton/LLM-research-assistant.git
cd LLM-research-assistant
pip install -r requirements.txt
```

---

### 🔐 Environment Setup

Create a `.env` file in the root of your project:

```env
OPENAI_API_KEY=your_openai_key_here
```

This key is required for both embeddings and chat completions.

---

## 🧪 Run Locally

```bash
streamlit run app.py
```

---

## 🌐 Deploying on Streamlit Cloud

This app is fully compatible with Streamlit Cloud:

- No compiled libraries required
- All dependencies are pure Python
- Automatically loads environment variables from `.env` if present

You may need to:
- Add `OPENAI_API_KEY` to Streamlit Cloud’s Secrets manager

---

## 📁 Folder Structure

```
LLM-research-assistant/
├── app.py
├── components/
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── embedding_store.py
│   ├── summarizer.py
│   └── qa_engine.py
├── data/
│   └── uploaded_files/        # Ignored in Git
├── .env                       # Local secrets
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Example Use Cases

- Quickly summarize long research papers
- Extract insights from technical documentation
- Build a reading list from a news article
- Create semantic search tools for private knowledge bases

---

## 🧹 TODOs / Future Improvements

- [ ] Add source highlighting in answers
- [ ] Add PDF citation extraction
- [ ] Support multi-document ingestion
- [ ] Add Claude or local model fallback

---

## 🤝 Credits

Developed by [Joel D. Hamilton](https://github.com/joeldhamilton)

Inspired by the concept of combining LLMs, RAG pipelines, and friendly UX for real-time personal research assistance.
