from google.adk.tools import ToolContext


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


def grammar_history() -> list[str]:
    """
    Returns a list of learnt grammar rules. These can be used to build questions the student will be able to answer.

    Returns:
        list[str]: list of grammar rules the student has previously learnt.
    """
    return [
        "N-이에요/예요",
        "있다/없다",
        "V/A-아요/어요/해요",
        "V/A-았아요/었어요/했어요",
        "V/A-ㄹ/을 거예요",
        "V-ㄹ/을 수 있다/없다",
        "V려고 하다",
        "N처럼/N 같아요",
        "V/Aㄴ/는 것",
        "V/A-는 것 같아요",
        "N-보다",
    ]


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
