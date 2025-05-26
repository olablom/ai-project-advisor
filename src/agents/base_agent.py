from abc import ABC, abstractmethod


class BaseAgent(ABC):
    @abstractmethod
    def generate_idea(self, user_input):
        pass
