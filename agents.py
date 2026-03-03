"""Agent management module for Smartlead software."""


class Agent:
    """Represents a sales/support agent in Smartlead."""

    def __init__(self, agent_id: int, name: str, email: str):
        self.agent_id = agent_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Agent(id={self.agent_id}, name='{self.name}', email='{self.email}')"


class AgentManager:
    """Manages the list of agents in the Smartlead project."""

    def __init__(self):
        self._agents: list[Agent] = []

    def add_agent(self, name: str, email: str) -> Agent:
        agent_id = len(self._agents) + 1
        agent = Agent(agent_id=agent_id, name=name, email=email)
        self._agents.append(agent)
        return agent

    def get_agents(self) -> list[Agent]:
        return list(self._agents)

    def count(self) -> int:
        return len(self._agents)

    def get_names(self) -> list[str]:
        return [agent.name for agent in self._agents]

    def summary(self) -> str:
        lines = [f"Total agents: {self.count()}"]
        if self._agents:
            lines.append("Agent names:")
            for agent in self._agents:
                lines.append(f"  {agent.agent_id}. {agent.name} ({agent.email})")
        else:
            lines.append("No agents registered yet.")
        return "\n".join(lines)


def get_default_manager() -> AgentManager:
    """Returns an AgentManager pre-populated with the default project agents."""
    manager = AgentManager()
    manager.add_agent("Uday Paboju", "uday@smartlead.com")
    manager.add_agent("Ravi Kumar", "ravi@smartlead.com")
    manager.add_agent("Priya Sharma", "priya@smartlead.com")
    return manager
