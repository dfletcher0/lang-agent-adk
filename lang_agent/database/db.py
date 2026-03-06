from asynctinydb import JSONStorage, Query, TinyDB

# import asyncio
# import time

BASE_DB_PATH = "lang_agent/database/"
GRAMMAR_DB_PATH = BASE_DB_PATH + "grammar.db"
LEADERBOARD_DB_PATH = BASE_DB_PATH + "leaderboard.db"


def create_db(db_path: str) -> TinyDB:
    """
    Create & return a database reference at the specified path.
    """
    try:
        db = TinyDB(
            db_path,
            storage=JSONStorage,
            ensure_ascii=False,
            sort_keys=True,
            indent=4,
            separators=(",", ": "),
        )
        return db
    except FileNotFoundError:
        raise Exception(f"invalid path {db_path} specified for database.")


GRAMMAR_DB = create_db(GRAMMAR_DB_PATH)
LEADERBOARD_DB = create_db(LEADERBOARD_DB_PATH)
