# --- --- ---

.PHONY: install
install:
	@poetry install


.PHONY: test
test:
	poetry run pytest


.PHONY: check
check:
	@poetry check --lock
	@poetry run ruff check --fix
	@poetry run ruff format

# --- --- ---

.PHONY: serve
serve:
	poetry run python -m twon_ranker.api
