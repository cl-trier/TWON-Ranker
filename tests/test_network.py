import logging
from typing import List

from src import modules, schemas


def test_network_is_follower(user: schemas.User, posts: List[schemas.Post]):
    results = modules.NetworkAnalysis().is_follower(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([post.author_id in user.follower for post in posts if results[post.id] == 1])


def test_network_is_following(user: schemas.User, posts: List[schemas.Post]):
    results = modules.NetworkAnalysis().is_following(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([post.author_id in user.following for post in posts if results[post.id] == 1])


def test_network_likes_count(user: schemas.User, posts: List[schemas.Post]):
    results = modules.NetworkAnalysis().likes_count(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([results[post.id] == len(post.likes) for post in posts])


def test_network_comments_count(user: schemas.User, posts: List[schemas.Post]):
    results = modules.NetworkAnalysis().comments_count(user, posts)
    logging.info(results)

    assert set(results.keys()) == set([post.id for post in posts])
    assert all([results[post.id] == len(post.comments) for post in posts])
