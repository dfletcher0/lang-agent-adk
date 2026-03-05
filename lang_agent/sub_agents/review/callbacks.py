import logging
import time

from asynctinydb import Query
from asynctinydb import operations as ops
from google.adk.agents.callback_context import CallbackContext

from lang_agent.database.db import GRAMMAR_DB

logger = logging.getLogger(__name__)


async def before_review_agent_callback(callback_context: CallbackContext) -> None:
    """
    Updates the grammar database to set grammar rules before the review_agent executes.
    """
    grammar_rules_tested = callback_context.state.get("grammar_rules", [])
    grammar_table = GRAMMAR_DB.table("grammar")
    time_tested = time.time()

    for tested_rule in grammar_rules_tested:
        logger.debug(f"Updating grammar rule: {tested_rule}, last_tested: {time_tested}")

        Rule = Query()
        await grammar_table.update(
            ops.set("last_tested", time_tested), Rule.rule == tested_rule
        )
        await grammar_table.update(ops.add("times_tested", 1), Rule.rule == tested_rule)

    return None
