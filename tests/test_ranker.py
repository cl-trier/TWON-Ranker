import logging
from typing import List, Dict

from src import Ranker
from src.schemas import User, Post


def test_ranker(user: User, posts: List[Post], weights: Dict[str, float]):
    logging.info(Ranker()(user, posts, weights))
