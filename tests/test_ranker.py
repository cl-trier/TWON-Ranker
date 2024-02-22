import logging
import typing

from src import Ranker
from src.post import Post
from src.request import Request


def test_ranker(posts: typing.List[Post]):
    logging.info(Ranker()(Request(items=posts)).ranking_map)
