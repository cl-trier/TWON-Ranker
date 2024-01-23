from typing import List, Dict

from fastapi import FastAPI

from src import Ranker, Response
from src.schemas import User, Post
from .config import Config

app = FastAPI(
    title=Config.title,
    description=open(f'{Config.docs_path}/index.md').read(),
    version=Config.version,
    docs_url='/'
)

ranker = Ranker(log_path=Config.log_path)


@app.post(
    "/rank/",
    summary='todo',
    description=open(f'{Config.docs_path}/rank.md').read()
)
async def rank(
        user: User, posts: List[Post], weights: Dict[str, float]
) -> Response:
    return ranker(user, posts, weights)
