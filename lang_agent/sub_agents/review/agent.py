from google.adk.agents import LlmAgent
from google.genai import types

# from lang_agent.sub_agents.review.tools import get_answers, grade_answers
from pydantic import BaseModel, Field

from .prompts import REVIEW_AGENT_PROMPT

# from lang_agent.sub_agents.review.tools import grammar_history, save_answer, vocab_search


class TestFeedback(BaseModel):
    q_num: int = Field(
        description="The question number that the feedback is associated with."
    )
    grade: int = Field(
        description="An integer between 0 and 100. Do not use percentages. Represents the score awarded for the student's answer to the question."
    )
    feedback: str = Field(
        description="A short 2-3 sentence summary of the accuracy of the student's answer to the question, including a better answer, if available."
    )


class FeedbackOutput(BaseModel):
    grades: list[TestFeedback]
    overall_feedback: str = Field(
        description="Overall feedback on the student's performance across the entire test, including strengths and weaknesses. Max 200 words."
    )


review_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="review_agent",
    description="An agent responsible for reviewing quiz answers, grading them on accuracy, and providing feedback.",
    instruction=REVIEW_AGENT_PROMPT,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2  # keep the model's output mostly factual
    ),
    output_schema=FeedbackOutput,
    output_key="test_feedback",
)

# tools=[
#     get_answers,
#     grade_answers,
# ]
