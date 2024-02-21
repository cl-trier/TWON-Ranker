import datetime
import typing

from pydantic import BaseModel

from .shared import Post_ID


class Post(BaseModel):
    id: Post_ID
    timestamp: datetime.datetime

    likes: typing.List[datetime.datetime] = []
    dislikes: typing.List[datetime.datetime] = []
    comments: typing.List['Post'] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                dict(
                    id='00001',
                    timestamp=datetime.datetime.now() - datetime.timedelta(hours=8),
                    likes=[
                        datetime.datetime.now() - datetime.timedelta(hours=6),
                        datetime.datetime.now() - datetime.timedelta(hours=2),
                    ],
                    dislikes=[
                        datetime.datetime.now() - datetime.timedelta(hours=3),
                        datetime.datetime.now() - datetime.timedelta(hours=1),
                    ],
                    comments=[
                        dict(
                            id='00002',
                            timestamp=datetime.datetime.now() - datetime.timedelta(hours=4),
                            likes=[
                                datetime.datetime.now() - datetime.timedelta(hours=2),
                            ],
                            dislikes=[
                                datetime.datetime.now() - datetime.timedelta(hours=1),
                            ],
                        )
                    ]
                )
            ]
        }
    }

    def __hash__(self):
        return hash(self.id)
