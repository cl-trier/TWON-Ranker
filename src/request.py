import datetime
import typing

import pydantic

from src import model
from src import modules


class Weights(pydantic.BaseModel):
    likes: float = 1.
    dislikes: float = 1.
    comments: float = 1.

    comments_likes: float = 1.
    comments_dislikes: float = 1.


class Request(pydantic.BaseModel):
    timestamp: datetime.datetime

    items: typing.List[model.Post]

    weights: Weights
    decay: modules.Decay
    noice: modules.Noice
