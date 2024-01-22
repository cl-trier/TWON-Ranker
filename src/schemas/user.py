from typing import List

from pydantic import BaseModel

from . import Post
from .shared import Author_ID


class User(BaseModel):
    id: Author_ID
    following: List[Author_ID]
    follower: List[Author_ID]

    posts: List[Post]

    model_config = {
        "json_schema_extra": {
            "examples": [
                dict(
                    id='1',
                    following=['2', '3', '4'],
                    follower=['2', '3'],
                    posts=[
                        Post(
                            id='101',
                            author_id='1',
                            content='Strawberry cheesecake milkshake from the sweet spot, Virginia Beach',
                        ),
                        Post(
                            id='102',
                            author_id='1',
                            content='What do you think of this yummy baklava?',
                        ),
                        Post(
                            id='103',
                            author_id='1',
                            content='Death by Caramel Cheesecake for Mother\'s Day lunch.',
                        ),
                        Post(
                            id='104',
                            author_id='1',
                            content='I made a velveteen rabbit red velvet cake for a friend\'s birthday',
                        )
                    ]
                )
            ]
        }
    }
