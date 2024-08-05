import datetime
import math
import typing

from twon_ranker import modules

REFERENCE_DATETIME: datetime.datetime = datetime.datetime.now()
REFERENCE_TIMEDELTA: datetime.timedelta = datetime.timedelta(days=3)
N: int = 1_000

DATETIME_NOW = datetime.datetime.now()

OBSERVATIONS: typing.List[datetime.datetime] = [
    REFERENCE_DATETIME - (REFERENCE_TIMEDELTA * i / N) for i in reversed(range(N))
]


def test_count_abs():
    assert (
        modules.Engagement(func="count_based", log_normalize=False)(items=OBSERVATIONS)
        == N
    )


def test_count_log():
    assert modules.Engagement(func="count_based", log_normalize=True)(
        items=OBSERVATIONS
    ) == math.log(N)
