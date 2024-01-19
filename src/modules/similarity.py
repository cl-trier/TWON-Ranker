from typing import List

import torch
from transformers import AutoTokenizer, AutoModel

from ..schemas import User, Post
from ..schemas.shared import RankingMap


class SimilarityComputer:
    # https://huggingface.co/Twitter/twhin-bert-base
    # https://arxiv.org/abs/2209.07562

    def __init__(self, slug: str = 'Twitter/twhin-bert-base'):
        """
        Initializes the object with a specified slug.

        Parameters:
            slug (str): The slug to be used for initializing the object. Defaults to 'Twitter/twhin-bert-base'.

        Returns:
            None
        """
        self.tokenizer = AutoTokenizer.from_pretrained(slug)
        self.model = AutoModel.from_pretrained(slug)

    def __call__(
            self,
            user: User,
            timeline_posts: List[Post],
            base: float = 10.,
            p_norm: float = 2.
    ) -> RankingMap:
        """
        Calculate the ranking map for a given user based on the similarity between the user's posts and the posts in the timeline.

        Args:
            user (User): The user object representing the user whose ranking map is being calculated.
            timeline_posts (List[Post]): The list of posts in the timeline.
            base (float, optional): The base value for the similarity calculation. Defaults to 10.
            p_norm (float, optional): The p-norm value for the similarity calculation. Defaults to 2.

        Returns:
            RankingMap: A dictionary containing the post IDs as keys and their corresponding similarity scores as values.
        """
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
        """
        Calculate the forward pass of the model.

        Args:
            batch (List[str]): A list of input strings.

        Returns:
            torch.tensor: The output tensor of the forward pass.
        """
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
        """
        Compute the similarity between centroids and points using a given base and p-norm.

        Args:
            centroids (torch.Tensor): A tensor containing the centroids.
            points (torch.Tensor): A tensor containing the points.
            base (float): The base value to subtract from the pairwise distance.
            p_norm (float): The p-norm value to use when computing the pairwise distance.

        Returns:
            torch.Tensor: A tensor containing the computed similarities.
        """
        return base - torch.nn.PairwiseDistance(p=p_norm)(
            points,
            (
                centroids
                .mean(dim=0)
                .repeat(centroids.size(0), 1)
            )
        )
