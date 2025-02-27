# Codebasics Q&A Chatbot 🌱

This project is a Q&A chatbot powered by LangChain, ChromaDB, and Gemini AI. It allows users to ask questions about Codebasics courses, and it retrieves relevant answers from a knowledge base.

## 🚀 Features

- Upload CSV with FAQs and store them in a ChromaDB vector database
- Google Gemini AI for generating answers
- LangChain RetrievalQA for querying the vector database
- Streamlit UI for an interactive experience

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/SHAIK-07/QA_Chot_bot.git
    cd codebasics-qa-chatbot
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate    # For macOS/Linux
    venv\Scripts\activate       # For Windows
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys**
    Create a `.env` file and add your Google Gemini API key:
    ```ini
    GOOGLE_API_KEY=your_google_api_key
    ```

## 🔹 Usage

Run the Streamlit App:
```bash
streamlit run app.py
```
- Click "Create Knowledgebase" to generate ChromaDB.
- Type your question in the text box.
- Get relevant answers based on the uploaded FAQs!

## 🛠 Project Structure

```bash
📂 codebasics-qa-chatbot
│── 📄 app.py                 # Streamlit app for user interaction
│── 📄 helper.py              # Core logic: vector DB creation & retrieval
│── 📄 requirements.txt       # List of dependencies
│── 📄 .env                   # API keys (ignored in Git)          
│── 📄 README.md              # Project documentation
```

## ⚙️ Tech Stack

- Google Gemini AI (text generation & embeddings)
- LangChain (retrieval & querying)
- ChromaDB (vector database)
- Streamlit (interactive UI)
- Python

## 🚀 Future Enhancements

- Hybrid Search (Keyword + Embeddings)
- Multi-question handling in one input
- Chat history & session memory

## 📢 Contributing

Feel free to contribute! Fork the repo, create a branch, and submit a PR.


## ⭐ Credits
This project was inspired by the Codebasics YouTube Channel. Special thanks to Dhaval Patel and his amazing content on Data Science, AI, and Machine Learning! 🚀

👉 Check out Codebasics here:
📺 [YouTube Channel](https://www.youtube.com/c/Codebasics)
🌍 [Website](https://codebasics.io/)