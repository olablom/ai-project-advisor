from core.ai_agent import AIAgent
from core.debate_manager import DebateManager
import yaml
import json


def main():
    # Define agent personas (replace with your own if you want)
    personas = [
        (
            "PortfolioBuilder",
            "You are PortfolioBuilder – an AI assistant that helps students create project ideas that will look impressive in their GitHub portfolios. You prioritize visual impact, modern frontend/backend tools, and high 'wow'-factor. You don't worry about deadlines or simplicity.",
        ),
        (
            "GradeOptimizer",
            "You are GradeOptimizer – an AI assistant that helps students create project ideas that maximize their chances of getting the highest possible grade. You focus on technical depth, advanced methods, and fulfilling grading criteria. You don't worry about job market or visual appeal.",
        ),
        (
            "CareerCoach",
            "You are CareerCoach – an AI assistant that helps students create project ideas that maximize their employability and relevance for the job market. You focus on modern tools, frameworks, and skills that are in demand by employers. You don't worry about academic depth or visual wow-factor.",
        ),
        (
            "RealismExpert",
            "You are RealismExpert – an AI assistant that helps students create project ideas that are realistic, feasible, and deliverable within a limited timeframe. You focus on MVP (Minimum Viable Product), simplicity, and ensuring the project can be completed on time. You don't worry about trendiness or maximum technical depth.",
        ),
    ]
    agents = [AIAgent(name, persona) for name, persona in personas]
    debate = DebateManager(agents)
    user_prompt = input("Enter your project idea prompt: ")
    debate.conduct_debate(user_prompt)
    transcript = debate.get_transcript()
    # Save transcript to YAML and JSON
    with open("debate_transcript.yaml", "w", encoding="utf-8") as f:
        yaml.dump(transcript, f, allow_unicode=True, sort_keys=False)
    with open("debate_transcript.json", "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=2, ensure_ascii=False)
    print(
        "\nDebate transcript saved to debate_transcript.yaml and debate_transcript.json"
    )


if __name__ == "__main__":
    main()
