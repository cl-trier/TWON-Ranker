import logging
from typing import List, Dict

from src import Ranker, schemas


def test_ranker(user: schemas.User, posts: List[schemas.Post], weights: Dict[str, float]):
    logging.info(Ranker()(user, posts, weights))
