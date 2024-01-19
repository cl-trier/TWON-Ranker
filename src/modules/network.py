from typing import List

from ..schemas import Post, User
from ..schemas.shared import RankingMap


class NetworkAnalysis:

    @property
    def features_map(self) -> dict:
        return dict(
            is_follower=NetworkAnalysis.is_follower,
            is_following=NetworkAnalysis.is_following,
            likes_count=NetworkAnalysis.likes_count,
            comments_count=NetworkAnalysis.comments_count,
        )

    @staticmethod
    def is_follower(user: User, timeline_posts: List[Post]) -> RankingMap:
        return {post.id: int(post.author_id in user.follower) for post in timeline_posts}

    @staticmethod
    def is_following(user: User, timeline_posts: List[Post]) -> RankingMap:
        return {post.id: int(post.author_id in user.following) for post in timeline_posts}

    @staticmethod
    def likes_count(_: User, timeline_posts: List[Post]) -> RankingMap:
        return {post.id: len(post.likes) for post in timeline_posts}

    @staticmethod
    def comments_count(_: User, timeline_posts: List[Post]) -> RankingMap:
        return {post.id: len(post.comments) for post in timeline_posts}
