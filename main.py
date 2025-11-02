from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA

# 1️⃣ Caminho do PDF
CAMINHO_PDF = "./base_doc.pdf"  # coloque seu arquivo PDF aqui

# 2️⃣ Carregar o PDF
print("📄 Carregando documento PDF...")
loader = PyPDFLoader(CAMINHO_PDF)
docs = loader.load()

# 3️⃣ Dividir o texto em partes menores
print("✂️ Dividindo texto em chunks...")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 4️⃣ Gerar embeddings com Ollama
print("🧩 Gerando embeddings com Ollama...")
embedding_model = OllamaEmbeddings(model="all-minilm")

# 5️⃣ Criar o banco de dados vetorial FAISS
print("💾 Criando banco vetorial com FAISS...")
vectorstore = FAISS.from_documents(chunks, embedding_model)

# 6️⃣ Configurar o modelo de linguagem para responder perguntas
llm = OllamaLLM(model="llama3")

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# 7️⃣ Loop de perguntas
print("\n✅ Sistema pronto! Faça suas perguntas sobre o conteúdo do PDF.")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("❓ Pergunta: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        break

    print("\n💬 Gerando resposta...")

    prompt_em_portugues = (
        "Responda a esta pergunta baseando-se apenas no contexto fornecido e **sempre no idioma Português do Brasil**: " 
        f"{pergunta}"
    )

    resposta = qa.invoke({"query": prompt_em_portugues})

    # compatibilidade entre versões: pode vir como "answer" ou "result"
    output = resposta.get("answer") or resposta.get("result") or resposta
    print("\n💬 Resposta:", output)
    print("-" * 80)


