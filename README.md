# 🤖 AI Project Advisor

A CLI tool that helps AI/ML students generate, evaluate, and select realistic project ideas using specialized AI agents.

## 💡 What It Does

This system simulates a team of AI personas (agents) with different perspectives to suggest and vote on the most appropriate project idea for a student query.

## 🧠 Core Features

- 💬 Multi-agent architecture with 4 unique roles:

  - `PortfolioBuilder` – focuses on GitHub wow-factor
  - `GradeOptimizer` – targets top-grade technical depth
  - `CareerCoach` – prioritizes job market value
  - `RealismExpert` – ensures the project is feasible

- 🗳️ Voting system to select the most suitable idea
- 📤 Final output includes reasoning and agent comments
- 🧪 Simple unit test that checks for diversity in agent proposals

## 🚀 How to Use

# Activate virtual environment

source venv/Scripts/activate

# Run the main program

python src/main.py

ai-project-advisor/
├── src/
│ ├── agents/ # Agent roles and prompts
│ ├── core/ # Project generation and voting logic
│ └── main.py # CLI interface
├── tests/ # Unit tests
├── examples/ # Sample outputs (YAML/JSON)
├── docs/ # Technical report and documentation
