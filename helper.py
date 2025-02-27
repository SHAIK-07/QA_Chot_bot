import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma


# ✅ Load environment variables
load_dotenv()

# ✅ Initialize Gemini Model and Embeddings
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.1)
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

def create_vector_db():
    """ Load CSV, create Chroma vector database, and persist embeddings. """
    
    loader = CSVLoader(file_path="codebasics_faqs.csv", source_column='prompt')
    data = loader.load()

    # ✅ Create ChromaDB (auto-persistent)
    vector_db = Chroma.from_documents(
        documents=data, 
        embedding=embeddings, 
        persist_directory="chroma_db"
    )

def get_qa_chain():
    """ Load ChromaDB, set up retriever, and create RetrievalQA chain. """

    # ✅ Load ChromaDB with correct argument
    vector_db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

    # ✅ Create a retriever (fetch top 2 most similar docs)
    retriever = vector_db.as_retriever(search_kwargs={"k": 1})

    # ✅ Define custom prompt template
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
        In the answer, try to provide as much text as possible from the "response" section in the source document without making much changes.
        If the answer is not found in the context, kindly respond: 
        "I currently don't have knowledge about this, but I will update you once I have more information." 
        Do not generate an answer that is not in the context.

        CONTEXT: {context}

        QUESTION: {question}"""


    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # ✅ Create RetrievalQA chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,  # ✅ Fixed argument
        chain_type_kwargs={"prompt": PROMPT}
    )

    return chain

if __name__ == "__main__":
    # ✅ Create vector database (if not already created)
    create_vector_db()
    
    # ✅ Load RetrievalQA Chain
    chain = get_qa_chain()

    # ✅ Query the chain
    response = chain.invoke({"query": "Do you have a JavaScript course?"})

    # ✅ Print response
    print("\n🔹 **Answer:**", response["result"])
    
    # ✅ Print source documents (for debugging)
    print("\n📄 **Source Documents:**")
    for doc in response["source_documents"]:
        print(doc.page_content)
