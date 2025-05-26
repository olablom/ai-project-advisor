class DebateManager:
    def __init__(self, agents):
        self.agents = agents
        self.full_transcript = []

    def conduct_debate(self, user_prompt):
        # 1. Initial proposal from each agent
        print("\n--- Initial Proposals ---\n")
        for agent in self.agents:
            response = agent.generate_response(user_prompt)
            self.full_transcript.append(
                {"agent": agent.name, "turn": "proposal", "content": response}
            )
            print(f"{agent.name}:\n{response}\n")

        # 2. Rebuttal round: each agent sees others' proposals
        print("\n--- Rebuttal Round ---\n")
        for agent in self.agents:
            others = [a for a in self.agents if a != agent]
            rebuttal_prompt = "Here are the other agents' proposals:\n"
            for other in others:
                # Find the last proposal from this agent
                last_proposal = next(
                    (
                        entry["content"]
                        for entry in reversed(self.full_transcript)
                        if entry["agent"] == other.name and entry["turn"] == "proposal"
                    ),
                    "",
                )
                rebuttal_prompt += f"{other.name}: {last_proposal}\n"
            rebuttal_prompt += "Please provide your rebuttal or counter-argument."
            response = agent.generate_response(rebuttal_prompt)
            self.full_transcript.append(
                {"agent": agent.name, "turn": "rebuttal", "content": response}
            )
            print(f"{agent.name} (rebuttal):\n{response}\n")

        # 3. Final recommendation (optional)
        print("\n--- Final Recommendations ---\n")
        for agent in self.agents:
            final_prompt = (
                "Based on the debate so far, what is your final recommendation?"
            )
            response = agent.generate_response(final_prompt)
            self.full_transcript.append(
                {
                    "agent": agent.name,
                    "turn": "final_recommendation",
                    "content": response,
                }
            )
            print(f"{agent.name} (final recommendation):\n{response}\n")

    def get_transcript(self):
        return self.full_transcript
