from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .database.db import GRAMMAR_DB, LEADERBOARD_DB
from .prompts import QUIZ_AGENT_PROMPT
from .sub_agents.review.agent import review_agent
from .tools import build_get_grammar_history_tool, build_get_leaderboard_tool, save_answer, build_update_leaderboard_tool

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="An agent responsible for generating a set of Korean language test questions.",
    instruction=QUIZ_AGENT_PROMPT,
    tools=[
        build_get_grammar_history_tool(db=GRAMMAR_DB),
        save_answer,
        build_update_leaderboard_tool(db=LEADERBOARD_DB),
        build_get_leaderboard_tool(db=LEADERBOARD_DB),
        AgentTool(review_agent),
    ],
)
