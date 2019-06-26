PYTHON=python3.7
MAIN_FILE=__main__.py
SERVER_FILE=web/server.py

start:
	$(PYTHON) $(MAIN_FILE)

.PHONY: web

web:
	PYTHONPATH=. $(PYTHON) $(SERVER_FILE)
