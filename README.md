# Smartlead Software

A lead management platform built for the Buildathon project.

## Agents

This project currently has **3 agents** registered:

| # | Name | Email |
|---|------|-------|
| 1 | Uday Paboju | uday@smartlead.com |
| 2 | Ravi Kumar | ravi@smartlead.com |
| 3 | Priya Sharma | priya@smartlead.com |

## Usage

### List all agents

```python
from agents import get_default_manager

manager = get_default_manager()
print(manager.summary())
```

Output:
```
Total agents: 3
Agent names:
  1. Uday Paboju (uday@smartlead.com)
  2. Ravi Kumar (ravi@smartlead.com)
  3. Priya Sharma (priya@smartlead.com)
```

### Run from the command line

```bash
cd Buildathon_project1
python main.py
```

### Add a new agent programmatically

```python
from agents import AgentManager

manager = AgentManager()
manager.add_agent("Alice Smith", "alice@smartlead.com")
print(f"Agents: {manager.count()}")
print(f"Names: {manager.get_names()}")
```

## Project Structure

```
Buildathon_project1/
├── agents.py   # Agent class and AgentManager
└── main.py     # Entry point – prints agent count and names
```
