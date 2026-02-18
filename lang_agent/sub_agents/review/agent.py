from google.adk.agents import Agent
from lang_agent.sub_agents.review.prompts import REVIEW_AGENT_PROMPT
from lang_agent.sub_agents.review.tools import get_answers, grade_answers
# from lang_agent.sub_agents.review.tools import grammar_history, save_answer, vocab_search

review_agent = Agent(
    model='gemini-2.5-flash',
    name='review_agent',
    description="An agent responsible for reviewing quiz answers, grading them on accuracy, and providing feedback.",
    instruction=REVIEW_AGENT_PROMPT,
    tools=[
        get_answers,
        grade_answers,
    ]
)
