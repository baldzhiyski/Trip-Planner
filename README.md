# ✈️ Trip Planner AI with CrewAI, Poetry & Ollama

This is an AI-powered travel planning application using [CrewAI](https://github.com/joaomdmoura/crewAI), [Poetry](https://python-poetry.org/), and [Ollama](https://ollama.com) with free local LLMs like `mistral`.

## 📦 Features

- Plan a full 7-day travel itinerary
- Automatically choose the best city
- Get packing tips, travel costs, safety advice
- Uses multiple cooperative agents (Expert Planner, City Selector, Tour Guide)
- Runs locally with Ollama and open-source models

---

## ⚙️ Requirements

- Python 3.11 (not 3.12)
- Git (for cloning the repo)
- [Poetry](https://python-poetry.org/) (for dependency & environment management)
- [Ollama](https://ollama.com/) (to run LLMs locally)
- Model: `mistral` (or any Ollama-supported model)
- Account and API key from [Serper](https://serper.dev) → store in `.env` as `SERPER_API_KEY=your_key_here`

---

## 💠 Setup Instructions

### ✅ Step 1: Install Python 3.11

Install Python 3.11 from the [official site](https://www.python.org/downloads/release/python-3110/), and ensure it's added to your system PATH.

### ✅ Step 2: Install Poetry (Windows)

Open PowerShell and run:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Then **restart your terminal**.

Test if it works:

```bash
poetry --version
```

---

### ✅ Step 3: Clone This Repo

```bash
git clone https://github.com/your-username/trip-planner.git
cd trip-planner
```

---

### ✅ Step 4: Set Up the Environment

```bash
poetry install
```

> This installs all dependencies (CrewAI, LangChain, Ollama bindings, tools, etc.)

---

### ✅ Step 5: Activate the Environment

```bash
poetry env list
```

Then run the following path:

```bash
C:\Users\<your-user>\AppData\Local\pypoetry\Cache\virtualenvs\<your-env-name>\Scripts\activate.bat
```

Or use PowerShell:

```powershell
& "C:\Users\<your-user>\AppData\Local\pypoetry\Cache\virtualenvs\<your-env-name>\Scripts\Activate.ps1"
```

---

### ✅ Step 6: Install & Run Ollama

Download and install Ollama from: [https://ollama.com](https://ollama.com)

Then pull the model:

```bash
ollama pull mistral
```

Make sure Ollama is running in the background.

---

### ✅ Step 7: Add Serper API Key

Create a `.env` file in your project root with the following:

```dotenv
SERPER_API_KEY=your_serper_key_here
```

You can get your key from: [https://serper.dev](https://serper.dev)

---

### ✅ Step 8: Run the Application

Once your virtual environment is activated:

```bash
python main.py
```

Follow the prompts in your terminal to input:

- Your origin location
- Desired cities
- Travel date range
- Your interests

The AI agents will then generate a custom travel plan for you.

---

## Powered By

| Component         | Tech                     |
| ----------------- | ------------------------ |
| 🧠 LLM Backend    | Ollama + Mistral         |
| 👥 Agent System   | CrewAI                   |
| 📛 Prompt Logic   | LangChain                |
| 📦 Env Management | Poetry                   |
| 🛠️ Tools          | Search Tools, Calculator |

---
