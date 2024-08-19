FROM python:3.10-slim AS builder

RUN pip install poetry
RUN mkdir -p /app
COPY . /app

WORKDIR /app
RUN poetry install --without dev

FROM python:3.10-slim AS base

COPY --from=builder /app /app

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["fastapi", "run", "src/twon_ranker/api", "--proxy-headers", "--port", "8000"]