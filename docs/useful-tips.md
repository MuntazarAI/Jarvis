Useful tips for working with Jarvis

- Run tests: python -m pytest -q
- Create and activate virtualenv:
  - python3 -m venv .venv
  - source .venv/bin/activate
- Install requirements: pip install -r requirements.txt
- Quick start: ./scripts/start-jarvis.sh (make executable)
- Running specific modules:
  - python main.py
  - python jarvis.py

Project layout highlights
- core/ and brain/ contain the main agent logic
- plugins/ holds optional extensions
- data/ is a safe place for caches and downloaded models

Development tips
- Use an isolated virtualenv to avoid global package conflicts
- Run individual unit tests while developing: pytest tests/test_*.py -q
- When adding a new plugin, add docs entry in docs/ and a quick usage example

If you'd like, these tips can be expanded into a developer guide with commands and examples.