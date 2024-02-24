import datetime
import typing

import pydantic

from src import modules
from src.post import Post


class Weights(pydantic.BaseModel):
    likes: float = 1.
    dislikes: float = 1.
    comments: float = 1.

    comments_likes: float = 1.
    comments_dislikes: float = 1.


class Request(pydantic.BaseModel):
    items: typing.List[Post]

    reference_datetime: datetime.datetime = datetime.datetime.now()

    weights: Weights = Weights()
    decay: modules.Decay = modules.Decay(minimum=.2, reference_timedelta=datetime.timedelta(days=3))
    noise: modules.Noise = modules.Noise(low=0.6, high=1.4)

    observation_score: typing.Literal['count_based', 'decay_based'] = 'count_based'
    observation_log_normalize: bool = False
