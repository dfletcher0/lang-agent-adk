import logging

from google.adk.tools import ToolContext

from lang_agent.database.db import GRAMMAR_DB

logger = logging.getLogger(__name__)


async def get_grammar_history(tool_context: ToolContext, num_rules: int) -> list[str]:
    """
    Returns 10 grammar rules that the student has learnt, ranked by how long ago they were last tested (oldest to newest).
    These can be used to build questions the student will be able to answer.

    Args:
        num_rules (int): The number of grammar rules to return.

    Returns:
        list[str]: list of 10 grammar rules the student has previously learnt.
    """
    # TODO: dependency injection here for testability
    logger.debug(f"grammar rules returned: {num_rules}")

    grammar_table = GRAMMAR_DB.table("grammar")
    all_results = await grammar_table.all()

    ranked_results = sorted(all_results, key=lambda x: x.get("last_tested", 0.0))[
        :num_rules
    ]

    logger.debug(ranked_results)

    ranked_results = [result.get("rule") for result in ranked_results]

    # Set the state
    tool_context.state["grammar_rules"] = ranked_results

    return ranked_results


def save_answer(
    tool_context: ToolContext,
    q_num: int,
    question: str,
    answer: str,
) -> None:
    """
    Saves the student's answer for later access.

    Args:
        q_num (int): The number of the question - e.g. 1 for the first question.
        question (str): The question that was generated for the student to answer.
        answer (str): The answer the student provided to the given question.
        grammar_rule (str): The grammar rule being tested.

    Returns:
        None
    """
    # TODO: Update to use session object
    logger.debug(f"Writing answer to state: {q_num}: Q) {question}\n A) {answer}")

    answers = tool_context.state.get("answers", {})
    answers[q_num] = {"question": question, "answer": answer}

    # re-assign the state object so that changes are detected
    tool_context.state["answers"] = answers
