from typing import List

import pytest

from src.post import Post


@pytest.fixture(scope='session', autouse=True)
def posts(request) -> List[Post]:
    return [Post(**example) for example in Post.model_config['json_schema_extra']['examples']]

