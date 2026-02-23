from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .prompts import QUIZ_AGENT_PROMPT
from .sub_agents.review.agent import review_agent
from .tools import grammar_history, save_answer, vocab_search

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="An agent responsible for generating a set of Korean language test questions.",
    instruction=QUIZ_AGENT_PROMPT,
    tools = [
        grammar_history,
        save_answer,
        AgentTool(review_agent),
    ]
)