import uvicorn

from twon_ranker.api import app


if __name__ == "__main__":
    uvicorn.run(app)
