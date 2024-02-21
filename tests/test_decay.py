import datetime

import pytest

from src import modules

MINIMUM: float = 0.2
INTERVAL: datetime.timedelta = datetime.timedelta(days=3)
TOL: float = 0.001

FUNCTION = modules.Decay(minimum=MINIMUM, interval=INTERVAL)


def test_now():
    datetime_now = datetime.datetime.now()
    assert FUNCTION(datetime_now, datetime_now) == pytest.approx(1., abs=TOL)


def test_max_past():
    datetime_now = datetime.datetime.now()
    datetime_past = datetime_now - INTERVAL
    assert FUNCTION(datetime_past, datetime_now) == pytest.approx(MINIMUM, abs=TOL)
