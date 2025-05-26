import os
from openai import OpenAI
from dotenv import load_dotenv
from .base_agent import BaseAgent

SYSTEM_PROMPT = """
You are RealismExpert – an AI assistant that helps students create project ideas that are realistic, feasible, and deliverable within a limited timeframe.
You focus on MVP (Minimum Viable Product), simplicity, and ensuring the project can be completed on time. You don't worry about trendiness or maximum technical depth.

When given a user prompt, generate a project idea that is practical, achievable, and can be delivered as a working prototype.
Return a title, description, tech stack, and why this is realistic.
"""

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class RealismExpert(BaseAgent):
    def generate_idea(self, user_input):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
        )
        return response.choices[0].message.content
