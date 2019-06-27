PYTHON=python3.7
MAIN_FILE=__main__.py
SERVER_FILE=web/server.py
CLIENT=web/pazaak-web

start:
	$(PYTHON) $(MAIN_FILE)

.PHONY: server

server:
	PYTHONPATH=. $(PYTHON) $(SERVER_FILE)

client:
	npm start --prefix $(CLIENT)
