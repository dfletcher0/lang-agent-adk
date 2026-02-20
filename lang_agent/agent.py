from google.adk.agents.llm_agent import LlmAgent
from lang_agent.prompts import ROOT_AGENT_PROMPT
from lang_agent.sub_agents.quiz.agent import quiz_agent
from lang_agent.sub_agents.review.agent import review_agent

root_agent = LlmAgent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description="An orchestration agent which routes the student's request to the relevant agent.",
    instruction=ROOT_AGENT_PROMPT,
    sub_agents=[
        quiz_agent,
        review_agent,
    ]
)

# 1. Implement review agent as tool on root agent. Instruct root agent to call it.
# 2. Refactor review agent to return structured output from 