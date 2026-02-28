## Code formatting
fmt:
	uv run black . && uv run isort .

## Run agent
eval:
	uv run adk eval lang_agent lang_agent/tests/eval/* --config_file_path lang_agent/tests/test_config.json --print_detailed_results

run:
	uv run main.py

run-adk:
	uv run adk run lang_agent

web:
	uv run adk web --port 8000