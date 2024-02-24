import datetime

import pytest

from src import modules

MINIMUM: float = 0.2
REFERENCE_TIMEDELTA: datetime.timedelta = datetime.timedelta(days=3)
TOL: float = 0.001

FUNCTION = modules.Decay(minimum=MINIMUM, reference_timedelta=REFERENCE_TIMEDELTA)

DATETIME_NOW = datetime.datetime.now()


def test_abs_now():
    assert FUNCTION(DATETIME_NOW, DATETIME_NOW) == pytest.approx(1., abs=TOL)


def test_abs_past():
    assert FUNCTION(DATETIME_NOW - REFERENCE_TIMEDELTA, DATETIME_NOW) == pytest.approx(MINIMUM, abs=TOL)
