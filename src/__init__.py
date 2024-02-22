import typing

from src import modules
from src.post import Post
from src.request import Request
from src.response import Response


class Ranker:

    def __init__(self, log_path: str = None):
        self.log_path = log_path

    def __call__(self, req: Request) -> Response:
        return Response(
            log_path=self.log_path,
            request=req,
            ranking_map={
                post.id: self.compute_post_score(req, post)
                for post in req.items
            }
        )

    @staticmethod
    def compute_post_score(req: Request, post: Post) -> float:

        observations: typing.List[float] = [
            weight * modules.Observations(items=items)(
                **dict(
                    func=req.observation_score,
                    log_normalize=req.observation_log_normalize,
                    reference_datetime=req.reference_datetime,
                    decay=req.decay
                )
            )
            for weight, items in
            [
                # post-based observations
                (req.weights.likes, post.likes),
                (req.weights.dislikes, post.dislikes),
                (req.weights.comments, post.comments_timestamp),

                # comments-based observations
                (req.weights.comments_likes, post.comments_likes),
                (req.weights.comments_dislikes, post.comments_dislikes),
            ]
        ]

        if req.observation_score == 'count_based':
            return req.noice() * req.decay(post.timestamp, req.reference_datetime) * sum(observations)

        else:
            return req.noice() * sum(observations)
