# --- --- ---

install:
	@python3 -m pip install -r requirements.txt

test:
	@python3 -m pytest tests/

# --- --- ---

dev:
	uvicorn api:app --reload

serve:
	uvicorn api:app
