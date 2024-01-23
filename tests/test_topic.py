import logging
from typing import List

from src import schemas, modules


def test_topic(user: schemas.User, posts: List[schemas.Post]):
    results = modules.TopicClassifier()(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all(0. <= score <= 1. for score in results.values())
