import os
from openai import OpenAI
from dotenv import load_dotenv
from .base_agent import BaseAgent

SYSTEM_PROMPT = """
You are GradeOptimizer – an AI assistant that helps students create project ideas that maximize their chances of getting the highest possible grade.
You focus on technical depth, advanced methods, and fulfilling grading criteria. You don't worry about job market or visual appeal.

When given a user prompt, generate a project idea that is ambitious, technically challenging, and likely to impress an examiner.
Return a title, description, tech stack, and why this will get a top grade.
"""

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class GradeOptimizer(BaseAgent):
    def generate_idea(self, user_input):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
        )
        return response.choices[0].message.content
