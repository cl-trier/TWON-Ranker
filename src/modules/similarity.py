from typing import List

import torch
from transformers import AutoTokenizer, AutoModel


class SimilarityComputer:
    # https://huggingface.co/Twitter/twhin-bert-base
    # https://arxiv.org/abs/2209.07562

    def __init__(self, slug: str = 'Twitter/twhin-bert-base'):
        self.tokenizer = AutoTokenizer.from_pretrained(slug)
        self.model = AutoModel.from_pretrained(slug)

    def __call__(self, history: List[str], timeline: List[str], p_norm: float = 2.):
        history_logits = self.embed(history)
        timeline_logits = self.embed(timeline)

        return torch.nn.PairwiseDistance(p=p_norm)(
            timeline_logits,
            (
                history_logits
                .mean(dim=0)
                .repeat(timeline_logits.size(0), 1)
            )
        )

    def embed(self, batch: List[str]):
        return (
            self.model(**self.tokenizer(batch, padding=True, return_tensors="pt"))
            .last_hidden_state[:, 0, :]
        )
