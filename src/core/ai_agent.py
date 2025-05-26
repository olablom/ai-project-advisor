import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AIAgent:
    def __init__(self, name, persona):
        self.name = name
        self.persona = persona
        self.conversation_history = [{"role": "system", "content": persona}]

    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def generate_response(self, user_input):
        self.add_message("user", user_input)
        response = client.chat.completions.create(
            model="gpt-4", messages=self.conversation_history
        )
        reply = response.choices[0].message.content.strip()
        self.add_message("assistant", reply)
        return reply
