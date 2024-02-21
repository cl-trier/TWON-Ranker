import typing

from src import model
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
    def compute_post_score(req: Request, post: model.Post) -> float:
        eps: float = req.noice()
        decay: float = req.decay(req.timestamp, post.timestamp)

        observations: typing.Dict[str, float] = {
            'likes': req.weights.likes * len(post.likes),
            'dislikes': req.weights.dislikes * len(post.dislikes),
            'comments': req.weights.comments * len(post.comments),
            'comments_likes': req.weights.comments_likes * sum([comment.likes for comment in post.comments]),
            'comments_dislikes': req.weights.comments_dislikes * sum([comment.dislikes for comment in post.comments]),
        }

        return eps * decay * sum(observations.values())
