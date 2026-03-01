from asynctinydb import JSONStorage, Query, TinyDB

# import asyncio
# import time


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


# async def main(db: TinyDB):
#     # answer = await db.search(Query().answer >= 42)
#     grammar = db.table("grammar")
#     await grammar.insert({"rule": "V-아/어/해서", "last_tested":time.time()})
#     results = await grammar.search(Query().rule == "아/어/해서")

#     return [dict(result) for result in results]

# if __name__ == "__main__":
#     db = create_db("lang_agent/database/test.db")
#     print(asyncio.run(main(db)))

# 1. Create DB *
# 2. Add initial documents (grammar rules) *
# 3. Add tool method to read ranked grammar rules from DB (initially hardcode DB, then look to dependency inject via ToolContext) *
# 4. Add tool method to update existing grammar rule most recently tested (epoch time int)
# 5. Update agent prompt to prioritise grammar rules which haven't been tested recently
# 6. Add tool method to add grammar rules to DB
# 6. Add to root_agent prompt to be able to teach new grammar rules (based on whats not in the db already) - then add them to the pool
# https://www.youtube.com/watch?v=GDm_uH6VxPY
