# 🤖 Sistema de Recuperação de Informações (RAG) Local

Este projeto implementa um sistema de **Geração Aumentada por Recuperação (RAG)**, permitindo responder a perguntas com base no conteúdo de um documento PDF, utilizando ferramentas *open-source* rodando totalmente localmente (on-premise).

O sistema é construído sobre a orquestração do **LangChain**, a eficiência do banco de dados vetorial **FAISS**, e a capacidade de processamento do **Ollama** para Embeddings e LLM.

## ✨ Tecnologias Utilizadas

| Componente | Tecnologia | Função no Projeto |
| :--- | :--- | :--- |
| **LLM & Embeddings** | **Ollama** | Executa o modelo `llama3` para geração de respostas e o `all-minilm` para vetorização de textos. |
| **Orquestração** | **LangChain** | Gerencia o pipeline RAG (carregamento, divisão, busca e resposta). |
| **Vector Database** | **FAISS** | Armazena e realiza buscas rápidas nos vetores (embeddings) do documento PDF. |
| **Processamento PDF** | **PyPDFLoader** | Responsável por ler e extrair o texto do arquivo de entrada. |

## 🛠️ Instalação e Configuração

### 1. Pré-requisitos

Para rodar o projeto, você deve ter instalado:
1.  **Ollama:** O serviço deve estar instalado e **ativo** (em `http://localhost:11434`).
2.  **Python:** Versão 3.10 ou superior.
3.  **Arquivo de Dados:** Um arquivo PDF nomeado **`base_doc.pdf`** na raiz do projeto.

### 2. Configuração de Modelos (Ollama)

Certifique-se de que os modelos de LLM e Embeddings foram baixados no seu Ollama:

```bash
ollama pull llama3
ollama pull all-minilm
```

### 3. Configuração do Ambiente Python

#### 1. Crie e Ative a Venv:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

#### 1. Instale as Dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute o Sistema

```bash
python main.py
```

Vídeo demonstrativo: [Link para o vídeo](https://www.loom.com/share/a547534677fc48e6b894978bd71a1345)