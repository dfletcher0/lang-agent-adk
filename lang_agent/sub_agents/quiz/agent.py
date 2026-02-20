from google.adk.agents import LlmAgent
from lang_agent.sub_agents.quiz.prompts import QUIZ_AGENT_PROMPT
from lang_agent.sub_agents.quiz.tools import grammar_history, save_answer, vocab_search

quiz_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="quiz_agent",
    description="An agent responsible for generating a set of Korean language test questions.",
    instruction=QUIZ_AGENT_PROMPT,
    tools = [
        grammar_history,
        save_answer,
    ]
)