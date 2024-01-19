from typing import List, Dict, Iterator, Set

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from ..schemas import User, Post
from ..schemas.shared import Post_ID, RankingMap


class TopicClassifier:
    # https://huggingface.co/cardiffnlp/tweet-topic-21-multi
    # https://arxiv.org/abs/2209.09824

    def __init__(self, slug: str = 'cardiffnlp/tweet-topic-21-multi'):
        self.tokenizer = AutoTokenizer.from_pretrained(slug)
        self.model = AutoModelForSequenceClassification.from_pretrained(slug)

        self.normalize_fn = torch.nn.Sigmoid()

    def __call__(
            self,
            user: User,
            timeline_posts: List[Post],
            theta: float = 0.5
    ) -> RankingMap:
        user_topics: Set[str] = set().union(*self.classify(user.posts, theta).values())

        return {
            pid: len(topics.intersection(user_topics)) / len(user_topics)
            for pid, topics in self.classify(timeline_posts, theta).items()
        }

    def classify(self, batch: List[Post], theta: float) -> Dict[Post_ID, Set[str]]:
        logits: torch.tensor = self.model_forward([post.content for post in batch])
        batch_label: torch.tensor = self.extract_label(logits, theta)

        return {post.id: post_label for post, post_label in zip(batch, batch_label)}

    def model_forward(self, batch: List[str]) -> torch.tensor:
        return self.model(**self.tokenizer(batch, padding=True, return_tensors="pt")).logits

    def extract_label(self, batch_logits: torch.tensor, theta: float) -> Iterator[Set[str]]:

        batch_norm_logits: torch.tensor = (self.normalize_fn(batch_logits) >= theta) * 1
        batch_ids: torch.tensor = [preds.nonzero().squeeze() for preds in torch.unbind(batch_norm_logits)]

        for post_ids in batch_ids:
            ids: List[int] | int = post_ids.tolist()

            if type(ids) is list:
                yield set(self.model.config.id2label[i] for i in ids)

            else:
                yield set([self.model.config.id2label[ids]])
