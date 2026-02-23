eval:
	uv run adk eval lang_agent lang_agent/tests/eval/*

run:
	uv run adk run lang_agent

web:
	uv run adk web --port 8000