import os
from openai import OpenAI
from dotenv import load_dotenv
from .base_agent import BaseAgent

SYSTEM_PROMPT = """
You are PortfolioBuilder – an AI assistant that helps students create project ideas that will look impressive in their GitHub portfolios.
You prioritize visual impact, modern frontend/backend tools, and high "wow"-factor. You don't worry about deadlines or simplicity.

When given a user prompt, generate a project idea that is flashy, trendy, and eye-catching, even if slightly ambitious.
Return a title, description, tech stack, and why this will impress.
"""

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class PortfolioBuilder(BaseAgent):
    def generate_idea(self, user_input):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
        )
        return response.choices[0].message.content
