import logging
import typing

from twon_ranker import Ranker
from twon_ranker.post import Post
from twon_ranker.request import Request


def test_ranker(posts: typing.List[Post]):
    logging.info(Ranker()(Request(items=posts)).ranking_map)
