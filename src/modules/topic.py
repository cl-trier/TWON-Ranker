from typing import List, Dict, Iterator, Set

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from ..schemas import User, Post
from ..schemas.shared import Post_ID, RankingMap


class TopicClassifier:
    # https://huggingface.co/cardiffnlp/tweet-topic-21-multi
    # https://arxiv.org/abs/2209.09824

    def __init__(self, slug: str = 'cardiffnlp/tweet-topic-21-multi'):
        """
        Initializes the object with the specified slug.

        Parameters:
            slug (str): The slug to use for initializing the class. Default value is 'cardiffnlp/tweet-topic-21-multi'.

        Returns:
            None
        """
        self.tokenizer = AutoTokenizer.from_pretrained(slug)
        self.model = AutoModelForSequenceClassification.from_pretrained(slug)

        self.normalize_fn = torch.nn.Sigmoid()

    def __call__(
            self,
            user: User,
            timeline_posts: List[Post],
            theta: float = 0.5
    ) -> RankingMap:
        """
        Calculates the ranking map for a given user and a list of timeline posts.

        Args:
            user (User): The user object for whom the ranking map is calculated.
            timeline_posts (List[Post]): The list of timeline posts to calculate the ranking map for.
            theta (float, optional): The threshold value for topic classification. Defaults to 0.5.

        Returns:
            RankingMap: A dictionary containing the ranking map, where the keys are post IDs and the values are the ranking scores.
        """
        user_topics: Set[str] = set().union(*self.classify(user.posts, theta).values())

        return {
            pid: len(topics.intersection(user_topics)) / len(user_topics)
            for pid, topics in self.classify(timeline_posts, theta).items()
        }

    def classify(self, batch: List[Post], theta: float) -> Dict[Post_ID, Set[str]]:
        """
        Classifies a batch of posts based on a given threshold.

        Args:
            batch (List[Post]): A list of posts to be classified.
            theta (float): The threshold value for classification.

        Returns:
            Dict[Post_ID, Set[str]]: A dictionary mapping post IDs to a set of classification labels.
        """
        logits: torch.tensor = self.model_forward([post.content for post in batch])
        batch_label: torch.tensor = self.extract_label(logits, theta)

        return {post.id: post_label for post, post_label in zip(batch, batch_label)}

    def model_forward(self, batch: List[str]) -> torch.tensor:
        """
        Calculate the forward pass of the model.

        Args:
            batch (List[str]): A list of input strings.

        Returns:
            torch.tensor: The output tensor of the forward pass.
        """
        return self.model(**self.tokenizer(batch, padding=True, return_tensors="pt")).logits

    def extract_label(self, batch_logits: torch.tensor, theta: float) -> Iterator[Set[str]]:
        """
        Extracts labels from batch logits based on a given threshold.

        Args:
            batch_logits (torch.tensor): The batch of logits.
            theta (float): The threshold value.

        Yields:
            Iterator[Set[str]]: An iterator that yields sets of labels.
        """
        batch_norm_logits: torch.tensor = (self.normalize_fn(batch_logits) >= theta).int()
        batch_ids: torch.tensor = [preds.nonzero().squeeze().tolist() for preds in torch.unbind(batch_norm_logits)]

        for post_ids in batch_ids:

            if isinstance(post_ids, list):
                yield {self.model.config.id2label[i] for i in post_ids}

            else:
                yield {self.model.config.id2label[post_ids], }
