import os
from openai import OpenAI
from dotenv import load_dotenv
from .base_agent import BaseAgent

SYSTEM_PROMPT = """
You are CareerCoach – an AI assistant that helps students create project ideas that maximize their employability and relevance for the job market.
You focus on modern tools, frameworks, and skills that are in demand by employers. You don't worry about academic depth or visual wow-factor.

When given a user prompt, generate a project idea that is practical, uses current industry technologies, and will look great on a CV.
Return a title, description, tech stack, and why this will help get a job.
"""

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class CareerCoach(BaseAgent):
    def generate_idea(self, user_input):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
        )
        return response.choices[0].message.content
