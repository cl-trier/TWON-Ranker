import logging
from typing import List

from src import modules, schemas


def test_similarity(user: schemas.User, posts: List[schemas.Post]):
    results = modules.SimilarityComputer()(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all(0. <= score <= 100. for score in results.values())
