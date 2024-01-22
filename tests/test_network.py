import logging
from typing import List

from src.modules import NetworkAnalysis
from src.schemas import User, Post


def test_network_is_follower(user: User, posts: List[Post]):
    results = NetworkAnalysis().is_follower(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([post.author_id in user.follower for post in posts if results[post.id] == 1])


def test_network_is_following(user: User, posts: List[Post]):
    results = NetworkAnalysis().is_following(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([post.author_id in user.following for post in posts if results[post.id] == 1])


def test_network_likes_count(user: User, posts: List[Post]):
    results = NetworkAnalysis().likes_count(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([results[post.id] == len(post.likes) for post in posts])


def test_network_comments_count(user: User, posts: List[Post]):
    results = NetworkAnalysis().comments_count(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([results[post.id] == len(post.comments) for post in posts])
