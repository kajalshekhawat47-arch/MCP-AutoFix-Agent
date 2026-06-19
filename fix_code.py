from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def fix_code(logs, code):

    prompt = f"""
You are a Python debugging expert.

Error Log:
{logs}

Python Code:
{code}

Fix the error.

Rules:
1. Return ONLY Python code.
2. Do not add explanations.
3. Preserve existing functionality.
4. Handle division by zero safely.
"""

    response = llm.invoke(prompt)

    return response.content