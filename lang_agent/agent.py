from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .prompts import QUIZ_AGENT_PROMPT
from .sub_agents.review.agent import review_agent
from .tools import get_grammar_history, get_leaderboard, save_answer, update_leaderboard

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="An agent responsible for generating a set of Korean language test questions.",
    instruction=QUIZ_AGENT_PROMPT,
    tools=[
        get_grammar_history,
        save_answer,
        update_leaderboard,
        get_leaderboard,
        AgentTool(review_agent),
    ],
)
