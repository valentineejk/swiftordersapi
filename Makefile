enter:
	cd .venv && source bin/activate
start:
	fastapi dev main.py
create-env:
	python -m venv .venv
