from typing import List

from pydantic import BaseModel

from .shared import Post_ID, Author_ID


class Post(BaseModel):
    id: Post_ID
    author_id: Author_ID
    content: str

    likes: List[Author_ID] = []
    comments: List[Post_ID] = []
