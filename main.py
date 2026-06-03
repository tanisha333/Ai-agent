import json
import os
import sys

from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import search_tool, wiki_tool, save_tool


load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_MODEL", "gemini-2.5-flash"),
    temperature=0.7
)

tools = [search_tool, wiki_tool, save_tool]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a research assistant that will help generate a research paper. "
        "Answer the user query and use necessary tools. "
        "Return a structured response with topic, summary, sources, and tools_used."
    ),
    response_format=ResearchResponse,
    debug=False,
)

if len(sys.argv) > 1:
    query = " ".join(sys.argv[1:]).strip()
else:
    try:
        query = input("What can I help you research? ").strip()
    except EOFError:
        print(
            "Please provide a research query, for example:\n"
            ".\\venv\\Scripts\\python.exe main.py \"What is the meaning of Pranav?\""
        )
        raise SystemExit(1)

if not query:
    print("Please provide a non-empty research query.")
    raise SystemExit(1)

try:
    raw_response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )
except ChatGoogleGenerativeAIError as exc:
    message = str(exc)
    if "RESOURCE_EXHAUSTED" in message or "429" in message:
        print(
            "Gemini did not return an answer because your API quota is exhausted.\n"
            "Wait for the quota window to reset, upgrade billing, or set a different "
            "model in .env, for example:\n"
            "GOOGLE_MODEL=gemini-2.5-flash-lite"
        )
    else:
        print(f"Gemini failed to return an answer: {exc}")
    raise SystemExit(1)

response = raw_response.get("structured_response", raw_response)
if isinstance(response, BaseModel):
    response = response.model_dump()

print(json.dumps(response, ensure_ascii=True, indent=2))
