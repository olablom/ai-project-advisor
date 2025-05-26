# 🤖 AI Project Advisor – Multi-Agent Debate System

A CLI tool that simulates a multi-turn debate between specialized AI agents, helping AI/ML students generate, evaluate, and select project ideas through structured argumentation and reflection.

## 💡 Overview

This system models a team of AI personas (agents) with distinct perspectives. Each agent participates in a multi-round debate, presenting proposals, rebuttals, and final recommendations. The full debate transcript is saved for analysis and reflection.

**Current Version:** Stable 4-agent system optimized for cost-effectiveness and reliability.

## 🧠 Core Features

- **Multi-turn, multi-agent debate:**
  - Each agent maintains its own conversation history and persona
  - Debate includes initial proposals, rebuttal/counter-argument round, and final recommendations
- **Four specialized agent roles:**
  - `PortfolioBuilder` – focuses on GitHub wow-factor and visual appeal
  - `GradeOptimizer` – targets top-grade technical depth and advanced methods
  - `CareerCoach` – prioritizes job market value and employer appeal
  - `RealismExpert` – ensures feasibility and deliverability within timeframes
- **Full debate transcript:**
  - Saved as both `debate_transcript.yaml` and `debate_transcript.json`
  - Includes all agent messages, turns, and reasoning for complete transparency
- **Cost-optimized design:**
  - ~$0.60 per complete debate (15,000-20,000 tokens)
  - 10-15 minute runtime for full analysis
  - Reliable performance without rate limiting issues

## 🚦 How It Works

1. **User prompt:** You enter a project idea or question (supports Swedish and English)
2. **Initial proposals:** Each agent generates 2-3 proposals based on its unique perspective
3. **Rebuttal round:** Each agent reviews others' proposals and provides counter-arguments
4. **Final recommendations:** Each agent gives a final recommendation based on the debate
5. **Transcript saved:** The full debate is logged for analysis and reporting

## 🚀 Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set your OpenAI API key:**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your-key-here
   ```
3. **Run the program:**
   ```bash
   python src/main.py
   ```
4. **Follow the prompts:**
   - Enter your project idea or question
   - Watch the debate unfold in the terminal
   - Review the full transcript in `debate_transcript.yaml` or `debate_transcript.json`

## 📦 Project Structure

```
ai-project-advisor/
├── src/
│   ├── core/
│   │   ├── ai_agent.py         # Agent class with persona & history
│   │   └── debate_manager.py   # Debate flow logic
│   ├── agents/                 # (Reserved for future agent definitions)
│   └── main.py                 # CLI entry point
├── tests/                      # Unit tests
├── examples/
│   └── sample_outputs/         # Example debate transcripts
├── docs/
│   └── technical_report.md     # Comprehensive system analysis
├── debate_transcript.yaml      # Latest debate output
├── debate_transcript.json      # Latest debate output (JSON format)
└── requirements.txt            # Python dependencies
```

## 🧩 System Evolution & Lessons Learned

### Current Stable Version (v1.0)

- **4 agents** with distinct, well-defined roles
- **Proven reliability** with consistent performance
- **Cost-effective** for regular use and demonstrations
- **Complete transparency** through detailed transcript logging

### Experimental v2.0 (Research Phase)

During development, we experimented with a 10-agent system featuring:

- 6 additional specialized agents (TechTrendAnalyst, UserExperienceAdvocate, etc.)
- Quantitative scoring across 6 criteria
- Consensus ranking system for top 3 project recommendations

**Key Findings:**

- **Scalability challenges:** 10 agents = 2.5x cost increase ($1.50+ per debate)
- **Rate limiting issues:** Hit OpenAI's token limits, causing system crashes
- **Diminishing returns:** Additional agents didn't proportionally improve decision quality

**Technical Solutions Developed:**

- Checkpoint/resume system for long-running processes
- Rate limiting with API call delays
- Hybrid model strategy (GPT-4 for critical reasoning, GPT-3.5-turbo for factual analysis)

See `docs/technical_report.md` for complete analysis of scalability challenges and solutions.

## 🎯 Usage Recommendations

- **For demonstrations:** Use current 4-agent system for reliable, cost-effective results
- **For research:** Experiment with agent configurations based on specific needs
- **For production:** Consider 4-6 agents as the optimal balance of perspective diversity and resource efficiency

## 📝 Example Output

Sample debate topics successfully processed:

- "Förslag på GitHub-projekt för AI-kurs" (Swedish)
- "Machine learning projects for portfolio building"
- "Full-stack web applications for job interviews"

See `examples/sample_outputs/` for complete debate transcripts.

## 🧠 Reflection & Analysis

The system demonstrates:

- **Emergent behavior** through agent interactions
- **Bias representation** via distinct agent personas
- **Conflict resolution** through structured debate
- **Decision transparency** via complete audit trails

Perfect for:

- Technical reports and academic analysis
- Understanding multi-agent system dynamics
- Exploring AI decision-making processes
- Demonstrating advanced AI orchestration concepts

## 🔧 Extending the System

- **Change agent roles:** Edit the `personas` list in `src/main.py`
- **Modify debate structure:** Extend `DebateManager` for additional rounds
- **Add new criteria:** Implement custom evaluation frameworks
- **Scale agents:** Add specialized agents for specific domains (with cost considerations)

---

_Built for advanced AI/ML coursework. Demonstrates practical multi-agent system design with real-world scalability insights._
