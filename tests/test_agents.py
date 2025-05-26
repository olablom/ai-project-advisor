import unittest
from src.agents.portfolio_builder import PortfolioBuilder
from src.agents.grade_optimizer import GradeOptimizer
from src.agents.career_coach import CareerCoach
from src.agents.realism_expert import RealismExpert


class TestAgents(unittest.TestCase):
    def test_agents_generate_different_ideas(self):
        user_input = "Test input"
        agents = [PortfolioBuilder(), GradeOptimizer(), CareerCoach(), RealismExpert()]
        ideas = [agent.generate_idea(user_input) for agent in agents]
        self.assertEqual(len(set(ideas)), 4)


if __name__ == "__main__":
    unittest.main()
