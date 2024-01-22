import logging
from typing import List

from src.modules import TopicClassifier
from src.schemas import User, Post


def test_topic(user: User, posts: List[Post]):
    results = TopicClassifier()(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all(0. <= score <= 1. for score in results.values())




