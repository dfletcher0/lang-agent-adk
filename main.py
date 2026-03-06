import asyncio
import logging
import uuid

from dotenv import load_dotenv
from google.adk.events import Event
from google.adk.runners import Runner
from google.adk.sessions import (
    BaseSessionService,
    InMemorySessionService,
    Session,
)
from google.genai.types import Content, Part

from lang_agent.agent import root_agent

# Configure environment
load_dotenv()
LOG_LEVEL = logging.DEBUG

# memory configuration
SQLITE_DB_URL = ""

# session configuration
APP_NAME = "lang_agent"
INTRO_MESSAGE = """Hello! I'm an examiner for Korean students. I can generate translation quizzes to test your Korean skills, and then give you feedback on your answers. 
Would you like a quiz with a specific number of questions or on a specific topic? Or do you want me to decide?"""
SESSION_FILE = f"{APP_NAME}/.session"
USER_ID = "abc"


def configure_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


logger = logging.getLogger(__name__)


async def create_or_resume_session(session_service: BaseSessionService) -> Session:
    try:
        with open(SESSION_FILE, "r") as f:
            session_id = f.read().strip()

        logger.info(f"Resuming session: {session_id}")
        session = await session_service.get_session(
            app_name=APP_NAME, user_id=USER_ID, session_id=session_id
        )

        return session

    except FileNotFoundError:
        logger.info("No existing session found. Creating a new one.")
        session = await session_service.create_session(
            app_name=APP_NAME, user_id=USER_ID
        )
        # with open(SESSION_FILE, "w") as f:
        #     f.write(session.id)

        return session


async def main():
    session_service = InMemorySessionService()
    session = await create_or_resume_session(session_service=session_service)

    # add introductory message to start of conversation
    intro_event = Event(
        author=root_agent.name,
        content=Content(role="model", parts=[Part(text=INTRO_MESSAGE)]),
        invocation_id=str(uuid.uuid4()),
        turn_complete=True,
    )
    await session_service.append_event(session=session, event=intro_event)

    runner = Runner(
        app_name=APP_NAME, agent=root_agent, session_service=session_service
    )

    print("Note: Type 'exit' to end the conversation.\n", "======================\n")
    print("Agent: " + INTRO_MESSAGE + "\n")

    # TODO: Resolve initial tool call warning
    # enter conversation loop:
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Exiting conversation...")
            break

        user_message = Content(role="user", parts=[Part(text=user_input)])

        async for event in runner.run_async(
            user_id=USER_ID, session_id=session.id, new_message=user_message
        ):
            if event.is_final_response():
                print(f"Agent: {event.content.parts[0].text}")


if __name__ == "__main__":
    configure_logging(level=LOG_LEVEL)
    asyncio.run(main())
