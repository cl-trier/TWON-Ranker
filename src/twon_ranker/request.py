import datetime
import typing

import pydantic

from twon_ranker import modules
from twon_ranker.post import Post


class Weights(pydantic.BaseModel):
    likes: float = 1.0
    dislikes: float = 1.0
    reposts: float = 1.0
    comments: float = 1.0

    comments_likes: float = 1.0
    comments_dislikes: float = 1.0


class Request(pydantic.BaseModel):
    mode: typing.Literal["ranked", "chronological", "random"] = "ranked"

    items: typing.List[Post]

    reference_datetime: datetime.datetime = datetime.datetime.now()

    decay: modules.Decay = modules.Decay(
        minimum=0.2, reference_timedelta=datetime.timedelta(days=3)
    )
    noise: modules.Noise = modules.Noise(low=0.6, high=1.4)
    engagement: modules.Engagement = modules.Engagement(
        func="count_based", log_normalize=False
    )

    weights: Weights = Weights()
