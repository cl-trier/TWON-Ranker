import logging
from typing import List

from src import Ranker
from src.schemas import User, Post


def test_ranker():
    user = User(
        id=1,
        following=[2, 3, 4],
        follower=[2, 3],
        posts=[
            Post(
                id=101,
                author_id=1,
                content='Strawberry cheesecake milkshake from the sweet spot, Virginia Beach',
            ),
            Post(
                id=102,
                author_id=1,
                content='What do you think of this yummy baklava?',
            ),
            Post(
                id=103,
                author_id=1,
                content='Death by Caramel Cheesecake for Mother\'s Day lunch.',
            ),
            Post(
                id=104,
                author_id=1,
                content='I made a velveteen rabbit red velvet cake for a friend\'s birthday',
            )
        ]
    )

    posts: List[Post] = [
        Post(
            id=201,
            author_id=2,
            content='I made Lemon Tiramisu for Mother\'s Day dessert. Yum!',
            likes=[1, 3],
            comments=[102]
        ),
        Post(
            id=301,
            author_id=3,
            content='Stack buttery slices of bread with prosciutto, brie and pear, then bake into a gooey, golden appetizer.',
            likes=[3, 4],
        ),
        Post(
            id=401,
            author_id=4,
            content='There are still American hostages held in Gaza. Biden isn\'t focused.',
            likes=[4, 5],
        ),
        Post(
            id=501,
            author_id=5,
            content='So disappointing another biological male stealing podium slots, medals, and financial opportunities for women in sports. This madness must stop.',
            likes=[5],
            comments=[]
        )
    ]

    logging.info(Ranker()(
        user,
        posts,
        weights=dict(
            similarity=0.75,
            topic=1.5,
            is_follower=.25,
            is_following=.75,
            likes_count=1.,
            comments_count=1.,
        )
    ))

