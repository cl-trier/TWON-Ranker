from typing import List

import torch
from transformers import AutoTokenizer, AutoModel

from ..schemas import User, Post
from ..schemas.shared import RankingMap


class SimilarityComputer:
    # https://huggingface.co/Twitter/twhin-bert-base
    # https://arxiv.org/abs/2209.07562

    def __init__(self, slug: str = 'Twitter/twhin-bert-base'):
        self.tokenizer = AutoTokenizer.from_pretrained(slug)
        self.model = AutoModel.from_pretrained(slug)

    def __call__(
            self,
            user: User,
            timeline_posts: List[Post],
            base: float = 10.,
            p_norm: float = 2.
    ) -> RankingMap:
        return {
            post.id: similarity for post, similarity in zip(
                timeline_posts, self.compute_similarity(
                    self.model_forward([post.content for post in user.posts]),
                    self.model_forward([post.content for post in timeline_posts]),
                    base, p_norm
                ).tolist()
            )
        }

    def model_forward(self, batch: List[str]) -> torch.tensor:
        return (
            self.model(**self.tokenizer(batch, padding=True, return_tensors="pt"))
            .last_hidden_state[:, 0, :]
        )

    @staticmethod
    def compute_similarity(
            centroids: torch.Tensor,
            points: torch.Tensor,
            base: float,
            p_norm: float
    ) -> torch.tensor:
        return base - torch.nn.PairwiseDistance(p=p_norm)(
            points,
            (
                centroids
                .mean(dim=0)
                .repeat(centroids.size(0), 1)
            )
        )
