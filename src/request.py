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

    decay: modules.Decay = modules.Decay(minimum=.2, reference_timedelta=datetime.timedelta(days=3))
    noise: modules.Noise = modules.Noise(low=.6, high=1.4)
    engagement: modules.Engagement = modules.Engagement(func='count_based', log_normalize=False)

    weights: Weights = Weights()
