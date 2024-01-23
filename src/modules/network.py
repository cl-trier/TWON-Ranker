from typing import List

from src import schemas


class NetworkAnalysis:

    @property
    def features_map(self) -> dict:
        """
        Get the features map of the class.

        Returns:
            dict: A dictionary mapping feature names to their corresponding methods.
        """
        return dict(
            is_follower=NetworkAnalysis.is_follower,
            is_following=NetworkAnalysis.is_following,
            likes_count=NetworkAnalysis.likes_count,
            comments_count=NetworkAnalysis.comments_count,
        )

    @staticmethod
    def is_follower(user: schemas.User, timeline_posts: List[schemas.Post]) -> schemas.shared.RankingMap:
        """
        Generate a ranking map indicating whether the author of each post in the timeline follows by the given user.

        Args:
            user (User): The user object representing the user.
            timeline_posts (List[Post]): The list of post objects representing the timeline posts.

        Returns:
            RankingMap: A dictionary mapping each post ID to a boolean indicating if the author is followed by the user.
        """
        return {post.id: int(post.author_id in user.follower) for post in timeline_posts}

    @staticmethod
    def is_following(user: schemas.User, timeline_posts: List[schemas.Post]) -> schemas.shared.RankingMap:
        """
        Generate a ranking map indicating whether the author of each post in the timeline is followed by the given user.

        Args:
            user (User): The user object representing the user.
            timeline_posts (List[Post]): The list of post objects representing the timeline posts.

        Returns:
            RankingMap: A dictionary mapping each post ID to a boolean indicating if the author is followed by the user.
        """
        return {post.id: int(post.author_id in user.following) for post in timeline_posts}

    @staticmethod
    def likes_count(_: schemas.User, timeline_posts: List[schemas.Post]) -> schemas.shared.RankingMap:
        """
        Generates a ranking map of the number of likes for each post in the timeline.

        Args:
            _: The User object (unused).
            timeline_posts: A list of Post objects representing the posts in the timeline.

        Returns:
            A RankingMap object containing the post IDs as keys and the number of comments as values.
        """
        return {post.id: len(post.likes) for post in timeline_posts}

    @staticmethod
    def comments_count(_: schemas.User, timeline_posts: List[schemas.Post]) -> schemas.shared.RankingMap:
        """
        Generates a ranking map of the number of comments for each post in the timeline.

        Args:
            _: The User object (unused).
            timeline_posts: A list of Post objects representing the posts in the timeline.

        Returns:
            A RankingMap object containing the post IDs as keys and the number of comments as values.
        """
        return {post.id: len(post.comments) for post in timeline_posts}
