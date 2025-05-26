from .base_agent import BaseAgent


class RealismExpert(BaseAgent):
    def generate_idea(self, user_input):
        return "RealismExpert generates an idea."
