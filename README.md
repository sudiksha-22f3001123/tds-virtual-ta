# TDS Virtual TA 

A **Virtual Teaching Assistant** for the **Tools in Data Science** course at **IIT Madras** BS Degree in Data Science and Applications


## Data Sources

- TDS Jan 2025 course content (as of 15 Apr 2025)
- Discourse posts (1 Jan – 14 Apr 2025)

## Tech Stack

- FastAPI (for backend API)
- LangChain (RAG pipeline)
- OpenAI / SentenceTransformers (for embeddings)
- FAISS / other vector store
- Vercel (for deployment)

## Project Structure
<pre><code> 
project/
├── downloaded_threads/       # Raw Discourse threads
├── markdown_files/           # Processed course content
├── preprocess.py             # Data prep script
├── app.py                    # FastAPI app
├── .env                      # API keys, etc.
├── requirements.txt          # Dependencies
└── vercel.json               # Vercel config
 </code></pre>

## License

This project is licensed under the MIT License - see the LICENSE file for details.
