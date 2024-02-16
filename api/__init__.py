from typing import List, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import Ranker, Response
from src.schemas import User, Post
from .config import Config

cfg = Config()

ranker = Ranker(log_path=cfg.log_path)

app = FastAPI(
    title=cfg.title,
    description=open(f'{cfg.docs_path}/index.md').read(),
    version=cfg.version,
    docs_url='/'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.trust_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(
    "/rank/",
    summary='todo',
    description=open(f'{cfg.docs_path}/rank.md').read()
)
async def rank(
        user: User, posts: List[Post], weights: Dict[str, float]
) -> Response:
    return ranker(user, posts, weights)
