import typing
import random
import datetime

from twon_ranker.post import Post
from twon_ranker.request import Request
from twon_ranker.response import Response

__all__ = ["Post", "Request", "Response", "Ranker"]


class Ranker:
    def __init__(self, log_path: str = None):
        self.log_path = log_path

    def __call__(self, req: Request) -> Response:
        return Response(
            log_path=self.log_path,
            request=req,
            ranking_map={
                post.id: self.compute_post_score(req, post) for post in req.items
            },
        )

    @staticmethod
    def compute_post_score(req: Request, post: Post) -> float:
        # handle baseline cases
        if req.mode == "random":
            return random.random()

        if req.mode == "chronological":
            return (post.timestamp - datetime.datetime(1970, 1, 1)).total_seconds()

        # req.mode == "ranked"
        observations: typing.List[float] = [
            weight
            * req.engagement(
                items=items, reference_datetime=req.reference_datetime, decay=req.decay
            )
            for weight, items in [
                # post-based observations
                (req.weights.likes, post.likes),
                (req.weights.dislikes, post.dislikes),
                (req.weights.reposts, post.reposts),
                (req.weights.comments, post.comments_timestamp),
                # comments-based observations
                (req.weights.comments_likes, post.comments_likes),
                (req.weights.comments_dislikes, post.comments_dislikes),
            ]
        ]

        if req.engagement.func == "count_based":
            return (
                req.noise()
                * req.decay(post.timestamp, req.reference_datetime)
                * sum(observations)
            )

        else:
            return req.noise() * sum(observations)
