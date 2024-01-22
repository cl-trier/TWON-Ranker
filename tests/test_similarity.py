import logging
from typing import List

from src.modules import SimilarityComputer
from src.schemas import User, Post


def test_similarity(user: User, posts: List[Post]):
    results = SimilarityComputer()(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all(0. <= score <= 100. for score in results.values())




