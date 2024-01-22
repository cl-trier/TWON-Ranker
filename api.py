from typing import List, Dict, Tuple

from fastapi import FastAPI

from src import Ranker
from src.schemas import User, Post
from src.schemas.shared import RankingMap

app = FastAPI(
    title='TWON RANKER API',
    description='todo',
    version='0.0.0',
)

ranker = Ranker()


@app.post(
    "/",
    summary='todo',
    description='todo'
)
async def rank(
        user: User, posts: List[Post], weights: Dict[str, float]
) -> Tuple[RankingMap, Dict[int, Dict[str, float]]]:
    return ranker(user, posts, weights)
