from typing import List, Dict

import pytest

from src import schemas


@pytest.fixture(scope='session', autouse=True)
def user(request) -> schemas.User:
    return schemas.User(**schemas.User.model_config['json_schema_extra']['examples'][0])


@pytest.fixture(scope='session', autouse=True)
def posts(request) -> List[schemas.Post]:
    return [schemas.Post(**example) for example in schemas.Post.model_config['json_schema_extra']['examples']]


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
