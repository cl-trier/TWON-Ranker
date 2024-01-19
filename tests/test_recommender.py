from typing import List

from src import Recommender
from src.schemas import User, Post, PostMetric


def test_recommender():
    user = User(
        id=1,
        following=[2, 3, 4],
        follower=[2, 3],
        posts=[
            Post(
                id=101,
                author_id=1,
                content='Strawberry cheesecake milkshake from the sweet spot, Virginia Beach',
                metrics=[PostMetric(label='likes', value=3)]
            ),
            Post(
                id=102,
                author_id=1,
                content='What do you think of this yummy baklava?',
                metrics=[PostMetric(label='likes', value=2)]
            ),
            Post(
                id=103,
                author_id=1,
                content='Death by Caramel Cheesecake for Mother\'s Day lunch.',
                metrics=[PostMetric(label='likes', value=1)]
            ),
            Post(
                id=104,
                author_id=1,
                content='I made a velveteen rabbit red velvet cake for a friend\'s birthday',
                metrics=[PostMetric(label='likes', value=4)]
            )
        ]
    )

    posts: List[Post] = [
        Post(
            id=201,
            author_id=2,
            content='I made Lemon Tiramisu for Mother\'s Day dessert. Yum!',
            metrics=[PostMetric(label='likes', value=1)]
        ),
        Post(
            id=301,
            author_id=3,
            content='Stack buttery slices of bread with prosciutto, brie and pear, then bake into a gooey, golden appetizer.',
            metrics=[PostMetric(label='likes', value=4)]
        ),
        Post(
            id=401,
            author_id=4,
            content='There are still American hostages held in Gaza. Biden isn\'t focused.',
            metrics=[PostMetric(label='likes', value=6)]
        ),
        Post(
            id=501,
            author_id=5,
            content='So disappointing another biological male stealing podium slots, medals, and financial opportunities for women in sports. This madness must stop.',
            metrics=[PostMetric(label='likes', value=2)]
        )
    ]

    Recommender()(user, posts)

