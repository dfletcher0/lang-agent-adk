from asynctinydb import Query
from google.adk.tools import ToolContext

from lang_agent.database.db import create_db

GRAMMAR_DB_PATH = "lang_agent/database/grammar.db"
GRAMMAR_DB = create_db(GRAMMAR_DB_PATH)


def vocab_search(term: str) -> list[dict[str, str]]:
    """
    Given a search term, returns learnt vocabulary which matches the search term most closely.

    Args:
        term (str): The vocabulary term to search for

    Returns:
        list[dict]: list of vocabulary terms the user has previously learnt which most closely match the search.
        These terms have an English translation ("eng" key) and a Korean translation ("kor" key).
    """
    return [
        {"kor": "고양이", "eng": "cat", "type": "noun"},
        {"kor": "공원", "eng": "park", "type": "noun"},
        {"kor": "달리기를 하다", "eng": "to run", "type": "verb"},
        {"kor": "걷다", "eng": "to walk", "type": "verb"},
    ]


async def get_grammar_history() -> list[str]:
    """
    Returns 10 grammar rules that the student has learnt, ranked by how long ago they were last tested (oldest to newest).
    These can be used to build questions the student will be able to answer.

    Returns:
        list[str]: list of 10 grammar rules the student has previously learnt.
    """
    # TODO: dependency injection here for testability
    grammar_table = GRAMMAR_DB.table("grammar")
    all_results = await grammar_table.all()

    ranked_results = sorted(
        all_results, key=lambda x: x.get("last_tested", 0.0), reverse=True
    )[:10]

    print(ranked_results)

    return [result.get("rule") for result in ranked_results]


def save_answer(
    tool_context: ToolContext, q_num: int, question: str, answer: str
) -> None:
    """
    Saves the student's answer for later access.

    Args:
        q_num (int): The number of the question - e.g. 1 for the first question.
        question (str): The question that was generated for the student to answer.
        answer (str): The answer the student provided to the given question.

    Returns:
        None
    """
    # TODO: Update to use session object
    answers = tool_context.state.get("answers", {})
    answers[q_num] = {"question": question, "answer": answer}

    # re-assign the state object so that changes are detected
    tool_context.state["answers"] = answers
