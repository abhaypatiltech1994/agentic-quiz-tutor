# 🧠 Agentic Quiz Tutor

An AI-powered, agentic quiz tutor built with **LangGraph** and **Groq LLM**. The agent intelligently fetches quiz questions and checks your answers using a tool-calling loop — no hard-coded logic, just a conversational AI doing the heavy lifting.

Supports both a **Streamlit web UI** and a **CLI** mode.

---

## ✨ Features

- 🤖 **Agentic AI** — Uses a LangGraph state machine with conditional tool-calling edges
- 📚 **Topic Filtering** — Ask for questions on a specific topic (e.g., "Azure", "DI")
- ✅ **Answer Checking** — Submits your answer and gets instant, intelligent feedback
- 🌐 **Streamlit Web UI** — Clean, interactive chat interface in the browser
- 💬 **CLI Mode** — Simple command-line conversation loop (run `agent.py` directly)
- ⚡ **Groq-powered** — Fast inference using Groq's LLM API (`openai/gpt-oss-20b`)

---

## 🏗️ Architecture

```
You (Browser / CLI)
   │
   ▼
[chatbot node]  ──── LLM decides ────►  [tools node]
      ▲                                      │
      └──────────── loops back ──────────────┘
```

The agent uses a **ReAct-style loop**:
1. You send a message.
2. The LLM decides whether to call a tool (`get_question_tool` or `check_answer_tool`).
3. The tool result is fed back to the LLM, which then responds to you.

---

## 📁 Project Structure

```
agentic-quiz-tutor/
├── agent.py          # LangGraph graph definition & CLI loop
├── app.py            # Streamlit web UI (chat interface)
├── tools.py          # Tool functions: get_question & check_answer
├── data/
│   ├── __init__.py
│   └── quiz_data.py  # Quiz question bank (QUIZ_BANK list)
├── requirements.txt  # Python dependencies
├── .env              # API keys (not committed to git)
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd agentic-quiz-tutor
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install langgraph langchain-core langchain-groq python-dotenv streamlit
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY="your_groq_api_key_here"
```

> Get your free API key at [https://console.groq.com](https://console.groq.com)

### 5. Run the app

**Web UI (recommended):**

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

**CLI mode:**

```bash
python agent.py
```

---

## 💬 Example Usage

```
You: Give me a question about Azure
Agent: What Azure service is used for serverless compute?

You: Azure Functions
Agent: Correct! The answer is 'Azure Functions'.

You: Give me a question about dependency injection
Agent: What is the .NET term for dependency injection container?

You: IServiceCollection
Agent: Correct! The answer is 'IServiceCollection'.
```

---

## 🛠️ Available Tools

| Tool | Description |
|------|-------------|
| `get_question_tool(topic)` | Fetches a random quiz question, optionally filtered by topic keyword |
| `check_answer_tool(user_answer)` | Checks the user's answer against the last question asked |

---

## 📝 Quiz Bank

The current quiz bank (`data/quiz_data.py`) covers:

| # | Topic | Question |
|---|-------|----------|
| 1 | Azure | What Azure service is used for serverless compute? |
| 2 | .NET DI | What is the .NET term for dependency injection container? |
| 3 | Azure AI | Which Azure service provides managed vector search for RAG apps? |
| 4 | Security | What does RBAC stand for? |
| 5 | ASP.NET Core | What is the default lifetime scope for a Scoped service? |

To add more questions, simply append entries to `QUIZ_BANK` in `data/quiz_data.py`:

```python
{"id": 6, "question": "Your question here?", "answer": "Your answer here"},
```

---

## 🧩 Tech Stack

| Library | Purpose |
|---------|---------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Agentic state machine / graph |
| [LangChain Core](https://python.langchain.com/) | Tool abstractions & message types |
| [langchain-groq](https://python.langchain.com/docs/integrations/chat/groq/) | Groq LLM integration (`openai/gpt-oss-20b`) |
| [Streamlit](https://streamlit.io/) | Web chat UI |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📄 License

MIT — feel free to use, modify, and share.
