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
├── downloaded_threads/     # Directory for storing downloaded Discourse threads
├── markdown_files/         # Directory for storing processed markdown files
├── .env                    # Environment variables (API keys, etc.)
├── preprocess.py           # Script for data collection and preprocessing
├── app.py                  # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore file
└── vercel.json             # Vercel deployment configuration
 </code></pre>

## License

This project is licensed under the MIT License 
