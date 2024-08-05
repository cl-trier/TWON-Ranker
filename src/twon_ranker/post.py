import datetime
import typing

import pydantic


class Post(pydantic.BaseModel):
    id: str
    timestamp: datetime.datetime

    likes: typing.List[datetime.datetime] = []
    dislikes: typing.List[datetime.datetime] = []
    reposts: typing.List[datetime.datetime] = []
    comments: typing.List["Post"] = []

    def __hash__(self):
        return hash(self.id)

    @pydantic.computed_field
    @property
    def comments_timestamp(self) -> typing.List[datetime.datetime]:
        return [comment.timestamp for comment in self.comments]

    @pydantic.computed_field
    @property
    def comments_likes(self) -> typing.List[datetime.datetime]:
        return [like for comment in self.comments for like in comment.likes]

    @pydantic.computed_field
    @property
    def comments_dislikes(self) -> typing.List[datetime.datetime]:
        return [dislike for comment in self.comments for dislike in comment.dislikes]

    model_config = {
        "json_schema_extra": {
            "examples": [
                dict(
                    id="P0001",
                    timestamp=datetime.datetime.now() - datetime.timedelta(hours=72),
                    likes=[
                        datetime.datetime.now() - datetime.timedelta(hours=68),
                        datetime.datetime.now() - datetime.timedelta(hours=42),
                    ],
                    dislikes=[
                        datetime.datetime.now() - datetime.timedelta(hours=40),
                        datetime.datetime.now() - datetime.timedelta(hours=24),
                    ],
                    reposts=[
                        datetime.datetime.now() - datetime.timedelta(hours=18),
                    ],
                    comments=[],
                ),
                dict(
                    id="P0002",
                    timestamp=datetime.datetime.now() - datetime.timedelta(hours=48),
                    likes=[
                        datetime.datetime.now() - datetime.timedelta(hours=36),
                        datetime.datetime.now() - datetime.timedelta(hours=24),
                    ],
                    dislikes=[
                        datetime.datetime.now() - datetime.timedelta(hours=32),
                        datetime.datetime.now() - datetime.timedelta(hours=18),
                    ],
                    reposts=[],
                    comments=[
                        dict(
                            id="C0001",
                            timestamp=datetime.datetime.now()
                            - datetime.timedelta(hours=20),
                            likes=[
                                datetime.datetime.now() - datetime.timedelta(hours=16),
                            ],
                            dislikes=[],
                        )
                    ],
                ),
                dict(
                    id="P0003",
                    timestamp=datetime.datetime.now() - datetime.timedelta(hours=8),
                    likes=[
                        datetime.datetime.now() - datetime.timedelta(hours=6),
                        datetime.datetime.now() - datetime.timedelta(hours=2),
                    ],
                    dislikes=[
                        datetime.datetime.now() - datetime.timedelta(hours=3),
                        datetime.datetime.now() - datetime.timedelta(hours=1),
                    ],
                    reposts=[
                        datetime.datetime.now() - datetime.timedelta(hours=12),
                        datetime.datetime.now() - datetime.timedelta(hours=32),
                    ],
                    comments=[
                        dict(
                            id="C0002",
                            timestamp=datetime.datetime.now()
                            - datetime.timedelta(hours=4),
                            likes=[
                                datetime.datetime.now() - datetime.timedelta(hours=2),
                            ],
                            dislikes=[
                                datetime.datetime.now() - datetime.timedelta(hours=1),
                            ],
                        ),
                        dict(
                            id="C0003",
                            timestamp=datetime.datetime.now()
                            - datetime.timedelta(hours=2),
                            likes=[],
                            dislikes=[
                                datetime.datetime.now() - datetime.timedelta(hours=1),
                            ],
                        ),
                    ],
                ),
            ]
        }
    }
