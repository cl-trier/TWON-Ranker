from typing import List

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class TopicClassifier:
    # https://huggingface.co/cardiffnlp/tweet-topic-21-multi
    # https://arxiv.org/abs/2209.09824

    def __init__(self, slug: str = 'cardiffnlp/tweet-topic-21-multi'):
        self.tokenizer = AutoTokenizer.from_pretrained(slug)
        self.model = AutoModelForSequenceClassification.from_pretrained(slug)

        self.normalize_fn = torch.nn.Sigmoid()

    def __call__(self, batch: List[str], theta: float = 0.5) -> List[List[str]]:
        logits = self.model(**self.tokenizer(batch, padding=True, return_tensors="pt")).logits

        norm_logits = (self.normalize_fn(logits) >= theta) * 1

        pred_ids = [preds.nonzero().squeeze() for preds in torch.unbind(norm_logits)]

        return [
            [self.model.config.id2label[idx] for idx in ids.tolist()]
            if type(ids.tolist()) == list else
            [self.model.config.id2label[ids.item()]]
            for ids in pred_ids
        ]
