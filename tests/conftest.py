from typing import List, Dict

import pytest

from src.schemas import User, Post


@pytest.fixture(scope='session', autouse=True)
def user(request) -> User:
    return User(**User.model_config['json_schema_extra']['examples'][0])


@pytest.fixture(scope='session', autouse=True)
def posts(request) -> List[Post]:
    return [Post(**example) for example in Post.model_config['json_schema_extra']['examples']]


@pytest.fixture(scope='session', autouse=True)
def weights(request) -> Dict[str, float]:
    return dict(
        similarity=0.75,
        topic=1.5,
        is_follower=.25,
        is_following=.75,
        likes_count=1.,
        comments_count=1.,
    )
