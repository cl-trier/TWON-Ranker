import typing

import pytest

from src import modules

LOW_BOUND: float = 0.8
HIGH_BOUND: float = 1.4

N: int = 1_000_000
TOL: float = 0.001

FUNCTION = modules.Noise(low=LOW_BOUND, high=HIGH_BOUND)
SAMPLES: typing.List[float] = FUNCTION.draw_samples(N)


def test_bounds():
    assert LOW_BOUND <= min(SAMPLES)
    assert max(SAMPLES) <= HIGH_BOUND


def test_distribution():
    assert sum(SAMPLES) / len(SAMPLES) == pytest.approx(sum([LOW_BOUND, HIGH_BOUND]) / 2, abs=TOL)
