from typing import List

import pytest

from src import model
from src.request import Weights


@pytest.fixture(scope='session', autouse=True)
def posts(request) -> List[model.Post]:
    return [model.Post(**example) for example in model.Post.model_config['json_schema_extra']['examples']]


@pytest.fixture(scope='session', autouse=True)
def weights(request) -> Weights:
    return Weights()
