import typing

import pytest

from src import modules

LOWER_LIMIT: float = 0.8
UPPER_LIMIT: float = 1.4

N: int = 1_000_000
TOL: float = 0.001

FUNCTION = modules.Noice(min=LOWER_LIMIT, max=UPPER_LIMIT)


def test_boundaries():
    assert LOWER_LIMIT <= FUNCTION() <= UPPER_LIMIT


def test_distribution():
    samples: typing.List[float] = [FUNCTION() for _ in range(N)]
    assert sum(samples) / len(samples) == pytest.approx(sum([LOWER_LIMIT, UPPER_LIMIT]) / 2, abs=TOL)
