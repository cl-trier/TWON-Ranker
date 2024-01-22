import logging
from typing import List

from fastapi.testclient import TestClient

from api import app
from src import Ranker
from src.schemas import User, Post


def test_api(user: User, posts: List[Post], weights):
    client = TestClient(app)

    api_results = client.post("/", json=dict(
        user=user.model_dump(),
        posts=[post.model_dump() for post in posts],
        weights=weights
    ))
    logging.info(api_results.json())

    assert Ranker()(user, posts, weights)[0] == api_results.json()[0]
    assert Ranker()(user, posts, weights)[1] == api_results.json()[1]
