from google.adk.agents.llm_agent import Agent
from lang_agent.prompts import ROOT_AGENT_PROMPT
from lang_agent.sub_agents.quiz.agent import quiz_agent
from lang_agent.sub_agents.review.agent import review_agent

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description="An orchestration agent which routes the student's request to the relevant agent.",
    instruction=ROOT_AGENT_PROMPT,
    sub_agents=[
        quiz_agent,
        review_agent,
    ]
)

# 0. Update `save_answers` tool to update state with answers *
#   - Validate if agent is generating all questions at once, or one at a time (at once is preferable: less API calls) *
# 1. Get review agent working
#   - A
#   - B