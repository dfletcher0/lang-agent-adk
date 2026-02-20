from google.adk.tools import ToolContext

# def get_answers(tool_context: ToolContext) -> dict:
#     """
#     Returns all answers submitted by the student for the current test.

#     Args:
#         None

#     Returns:
#         None
#     """
#     # TODO: Update to use session object
#     return tool_context.state.get("answers", {})

# def grade_answers(tool_context: ToolContext, grades: dict[int,float]) -> None:
#     """
#     Assigns a grade to an existing answer provided by the student.

#     Args:
#         grades (dict[int,float]): A grade dictionary, mapping the question number (int) to the grade for the question (float)

#     Returns:
#         None
#     """
#     # TODO: Update to use session object
#     answers = tool_context.state.get("answers", {})

#     for q in grades:
#         answers[q]["grade"] = grades[q]

#     # re-assign the state object so that changes are detected
#     tool_context.state["answers"] = answers