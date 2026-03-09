import time

import pytest

from lang_agent.tools import (
    build_get_grammar_history_tool,
    build_get_leaderboard_tool,
    build_update_leaderboard_tool,
    save_answer,
)


class MockTable:
    def __init__(self, initial=None):
        self._data = list(initial or [])

    async def all(self):
        return self._data

    async def insert(self, item):
        self._data.append(item)
        return item


class MockDB:
    def __init__(self, tables: dict = None) -> None:
        self._tables = {}
        for name, data in (tables or {}).items():
            self._tables[name] = MockTable(data)

    def table(self, name: str) -> list[dict]:
        if name not in self._tables:
            self._tables[name] = MockTable()
        return self._tables[name]


class DummyToolContext:
    def __init__(self):
        self.state = {}


@pytest.fixture
def mock_db():
    tables = {
        "grammar": [
            {"rule": "A", "last_tested": 100.0},
            {"rule": "B", "last_tested": 50.0},
            {"rule": "C", "last_tested": 150.0},
        ],
        "leaderboard": [
            {"time": 1, "score": 90},
            {"time": 2, "score": 70},
            {"time": 3, "score": 80},
            {"time": 4, "score": 60},
            {"time": 5, "score": 85},
            {"time": 6, "score": 75},
        ],
    }
    return MockDB(tables)


@pytest.fixture
def tool_context():
    return DummyToolContext()


@pytest.mark.asyncio
async def test_get_grammar_history_sets_state_and_returns_oldest_first(
    mock_db: MockDB, tool_context: DummyToolContext
):
    get_grammar_history = build_get_grammar_history_tool(mock_db)
    result = await get_grammar_history(tool_context, 2)

    # Expect oldest (lowest last_tested) first: B (50), A (100)
    assert result == ["B", "A"]
    assert tool_context.state["grammar_rules"] == ["B", "A"]


def test_save_answer_saves_answer(tool_context: DummyToolContext):
    save_answer(tool_context, 1, "이것은 뭐예요?", "Answer")
    assert 1 in tool_context.state["answers"]
    assert tool_context.state["answers"][1]["question"] == "이것은 뭐예요?"
    assert tool_context.state["answers"][1]["answer"] == "Answer"


@pytest.mark.asyncio
async def test_get_leaderboard_empty_returns_empty():
    db = MockDB({"leaderboard": []})
    get_leaderboard = build_get_leaderboard_tool(db)
    res = await get_leaderboard()
    assert res == []


@pytest.mark.asyncio
async def test_get_leaderboard_returns_top_five(mock_db):
    get_leaderboard = build_get_leaderboard_tool(mock_db)
    res = await get_leaderboard()

    # The implementation sorts descending and takes the top 5 highest scores
    expected = sorted(
        [result["score"] for result in mock_db.table("leaderboard")._data], reverse=True
    )[:5]
    assert res == expected


@pytest.mark.asyncio
async def test_update_leaderboard_inserts_score(mock_db):
    update_leaderboard = build_update_leaderboard_tool(mock_db)
    before = list(mock_db.table("leaderboard")._data)
    await update_leaderboard(33)
    data = mock_db.table("leaderboard")._data
    assert any(item.get("score") == 33 for item in data)
    assert len(data) == len(before) + 1
