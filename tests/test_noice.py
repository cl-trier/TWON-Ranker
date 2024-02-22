import typing

import pytest

from src import modules

LOW_BOUND: float = 0.8
HIGH_BOUND: float = 1.4

N: int = 1_000_000
TOL: float = 0.001

FUNCTION = modules.Noice(low=LOW_BOUND, high=HIGH_BOUND)


def test_boundaries():
    assert LOW_BOUND <= FUNCTION() <= HIGH_BOUND


def test_distribution():
    samples: typing.List[float] = FUNCTION.draw_samples(N)
    assert sum(samples) / len(samples) == pytest.approx(sum([LOW_BOUND, HIGH_BOUND]) / 2, abs=TOL)
