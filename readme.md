<h1 align="center">📊 DataPilot CSV Agent</h1>

<p align="center">
  🚀 Chat with your CSV data using LangChain + Groq LLM  
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=Talk+to+Your+Data;AI+Powered+CSV+Analysis;Agentic+Data+Assistant;LangChain+%2B+Groq+LLM" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/LangChain-Agentic%20AI-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Data-Analytics-yellow?style=for-the-badge"/>
</p>

---

## 📌 Overview

**DataPilot CSV Agent** is an **AI-powered data assistant** that allows users to interact with CSV files using natural language.

Instead of writing SQL or Python code, you can simply ask:

💬 *"What is the total revenue?"*  
💬 *"Show top 5 products by sales"*  
💬 *"Find trends in customer data"*  

---

## 🧠 Features

- 📊 Natural language querying on CSV data  
- 🤖 Agentic AI reasoning & decision-making  
- ⚡ Fast responses using Groq LLM  
- 🧠 Automatic data analysis & summarization  
- 🔍 Smart filtering, aggregation, and insights  
- 📈 Data-driven answers without coding  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|----------|--------|
| Python 🐍 | Core language |
| LangChain 🔗 | Agent framework |
| Groq ⚡ | Fast LLM inference |
| Pandas 📊 | Data processing |
| Streamlit 🎨 | UI (optional) |

---


## 📂 Project Structure
```
 csv-agent/
 app.py
 data.csv
 requirements.txt
 README.md
```

---

## ⚙️ Installation

```bash id="csvinstall"
pip install langchain langchain_groq pandas
```
## 🔑 Setup API Key
```python
import os
os.environ["GROQ_API_KEY"] = "your_api_key"
```
---
## 🧪 Example Usage
```python
import pandas as pd
from langchain_groq import ChatGroq

# Load CSV
df = pd.read_csv("data.csv")

# Initialize model
llm = ChatGroq(model="llama-3.3-70b-versatile")

query = "What are the top 5 highest sales?"

response = llm.invoke(query)

print(response.content)
```
---
)
## 📸 Demo
<p align="center"> <img src="https://media.giphy.com/media/l0HlQ7LRalQqdWfao/giphy.gif" width="500"/> </p>
---
### 🎯 Use Cases
---
📊 Business data analysis
🛒 Sales & revenue insights
📈 Trend detection
🧑‍💼 Decision support systems
🧠 AI-powered analytics dashboards
---
### 🔮 Future Scope
🧠 Memory-enabled conversations
📄 Multi-file (CSV + Excel) support
📊 Auto visualization (charts & graphs)
🤖 Multi-agent system
🌐 Web deployment (Streamlit / FastAPI)
---
## 🤝 Contributing
```bash
git checkout -b feature/new-feature
git commit -m "Added new feature"
git push origin feature/new-feature
```

## 👩‍💻 Author
Ashita Mendhe
📊 Data Analyst | 🤖 AI Engineer
---
📜 License

MIT License
---
