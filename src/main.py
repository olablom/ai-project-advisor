from agents.portfolio_builder import PortfolioBuilder
from agents.grade_optimizer import GradeOptimizer
from agents.career_coach import CareerCoach
from agents.realism_expert import RealismExpert
import json
import yaml

VOTING_PROMPT = """
You are {agent_name}. Here are four project proposals:
A: {PortfolioBuilder}
B: {GradeOptimizer}
C: {CareerCoach}
D: {RealismExpert}

Which project best matches your goal? Reply with the letter (A, B, C, or D) and a short motivation.
"""


def run_all_agents(user_prompt):
    agents = [PortfolioBuilder(), GradeOptimizer(), CareerCoach(), RealismExpert()]
    agent_names = ["PortfolioBuilder", "GradeOptimizer", "CareerCoach", "RealismExpert"]
    proposals = {}
    for agent, name in zip(agents, agent_names):
        proposals[name] = agent.generate_idea(user_prompt)
    return proposals


from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def vote_for_best_project(agent_name, proposals):
    prompt = VOTING_PROMPT.format(
        agent_name=agent_name,
        PortfolioBuilder=proposals["PortfolioBuilder"],
        GradeOptimizer=proposals["GradeOptimizer"],
        CareerCoach=proposals["CareerCoach"],
        RealismExpert=proposals["RealismExpert"],
    )
    response = client.chat.completions.create(
        model="gpt-4", messages=[{"role": "system", "content": prompt}]
    )
    content = response.choices[0].message.content.strip()
    if ":" in content:
        vote, motivation = content.split(":", 1)
        vote = vote.strip().upper()
        motivation = motivation.strip()
    else:
        vote = content.strip().upper()
        motivation = ""
    return vote, motivation


def main():
    user_prompt = input("Enter your project idea prompt: ")
    proposals = run_all_agents(user_prompt)
    print("\n💡 Project proposals from all agents:\n")
    for name, proposal in proposals.items():
        print(f"--- {name} ---\n{proposal}\n")

    agent_names = ["PortfolioBuilder", "GradeOptimizer", "CareerCoach", "RealismExpert"]
    votes = {}
    motivations = {}
    for agent_name in agent_names:
        vote, motivation = vote_for_best_project(agent_name, proposals)
        votes[agent_name] = vote
        motivations[agent_name] = motivation

    vote_map = {
        "A": "PortfolioBuilder",
        "B": "GradeOptimizer",
        "C": "CareerCoach",
        "D": "RealismExpert",
    }
    project_letter_map = {v: k for k, v in vote_map.items()}
    vote_counts = {letter: 0 for letter in ["A", "B", "C", "D"]}
    voting_summary = {}
    for agent, v in votes.items():
        voting_summary[agent] = f"Project {v}" if v in vote_map else v
        if v in vote_counts:
            vote_counts[v] += 1
    max_votes = max(vote_counts.values())
    winning_letters = [
        k for k, count in vote_counts.items() if count == max_votes and count > 0
    ]
    result = (
        f"Project {winning_letters[0]}"
        if len(winning_letters) == 1
        else "Tie - user should choose"
    )

    # Print voting summary in terminal
    print("\n🗳️ Voting Results:\n")
    for agent in agent_names:
        print(f"{agent} voted for: {voting_summary[agent]}")
    print(
        f"\n✅ Final decision: {result} ({max_votes} votes)"
        if len(winning_letters) == 1
        else f"\n⚠️ Tie between: {', '.join(['Project ' + l for l in winning_letters])}"
    )
    print("\n📌 Comments:")
    for agent in agent_names:
        print(f"- {agent}: {motivations[agent]}")

    # Prepare YAML output structure
    yaml_output = {
        "final_project": proposals[vote_map[winning_letters[0]]]
        if len(winning_letters) == 1
        else "Tie - user should choose",
        "voting_summary": {
            **voting_summary,
            "result": result,
            "votes_per_project": {
                f"Project {l}": vote_counts[l] for l in ["A", "B", "C", "D"]
            },
        },
        "agent_comments": motivations,
    }
    with open("output.yaml", "w", encoding="utf-8") as f:
        yaml.dump(yaml_output, f, allow_unicode=True, sort_keys=False)
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(yaml_output, f, indent=2, ensure_ascii=False)
    print("\nResults saved to output.yaml and output.json")


if __name__ == "__main__":
    main()
