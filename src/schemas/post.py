from typing import List

from pydantic import BaseModel

from .shared import Post_ID, Author_ID


class Post(BaseModel):
    id: Post_ID
    author_id: Author_ID
    content: str

    likes: List[Author_ID] = []
    comments: List[Post_ID] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                dict(
                    id='201',
                    author_id='2',
                    content='I made Lemon Tiramisu for Mother\'s Day dessert. Yum!',
                    likes=['1', '3'],
                    comments=['102']
                ),
                dict(
                    id='301',
                    author_id='3',
                    content='Stack buttery slices of bread with prosciutto, brie and pear, then bake into a gooey, golden appetizer.',
                    likes=['3', '4'],
                ),
                dict(
                    id='401',
                    author_id='4',
                    content='There are still American hostages held in Gaza. Biden isn\'t focused.',
                    likes=['4', '5'],
                ),
                dict(
                    id='501',
                    author_id='5',
                    content='So disappointing another biological male stealing podium slots, medals, and financial opportunities for women in sports. This madness must stop.',
                    likes=['5'],
                    comments=[]
                )
            ]
        }
    }

    def __hash__(self):
        return hash(str(self.id) + str(self.author_id) + self.content)
