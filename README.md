# AI Research Agent

An AI-powered research assistant built using LangChain and Google's Gemini model. The agent can search the web, retrieve information from Wikipedia, and generate structured research summaries.

## Features

* Web search using DuckDuckGo
* Wikipedia knowledge retrieval
* Structured JSON responses using Pydantic
* Tool-calling AI agent architecture
* Research result saving to text files
* Powered by Google Gemini

## Tech Stack

* Python
* LangChain
* Google Gemini API
* Pydantic
* DuckDuckGo Search
* Wikipedia API

## Project Structure

```text
AI-Agent/
│
├── main.py
├── tools.py
├── requirements.txt
├── .env
├── research_output.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/tanisha333/Ai-agent.git
cd Ai-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

## Running the Project

```bash
python main.py
```

Example:

```text
What can I help you research?
> What is Artificial Intelligence?
```

## Sample Output

```json
{
  "topic": "Artificial Intelligence",
  "summary": "Artificial Intelligence (AI) refers to systems capable of performing tasks that normally require human intelligence.",
  "sources": [
    "Wikipedia",
    "DuckDuckGo Search"
  ],
  "tools_used": [
    "wikipedia",
    "search"
  ]
}
```

## Future Improvements

* PDF report generation
* Arxiv research paper integration
* Streamlit web interface
* Multi-agent research workflow
* Citation generation

## Author

Tanisha N
Computer Science Student | AI & GenAI Enthusiast
