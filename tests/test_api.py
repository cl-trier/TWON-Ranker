import logging
from typing import List

from fastapi.testclient import TestClient

from api import app
from src import Ranker, schemas


def test_api(user: schemas.User, posts: List[schemas.Post], weights):
    client = TestClient(app)

    api_results = client.post("/rank/", json=dict(
        user=user.model_dump(),
        posts=[post.model_dump() for post in posts],
        weights=weights
    ))
    logging.info(api_results.json())

    assert Ranker()(user, posts, weights).ranking_map == api_results.json()['ranking_map']
    assert Ranker()(user, posts, weights).feature_table == api_results.json()['feature_table']
