from typing import List

from pydantic import BaseModel

from . import Post
from .shared import Author_ID


class User(BaseModel):
    id: Author_ID
    following: List[Author_ID]
    follower: List[Author_ID]

    posts: List[Post]
