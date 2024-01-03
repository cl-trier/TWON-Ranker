# https://huggingface.co/Twitter/twhin-bert-base
# https://arxiv.org/abs/2209.07562

# TwHIN: Embedding the Twitter Heterogeneous Information Network for Personalized Recommendation
# https://arxiv.org/pdf/2202.05387.pdf

# https://huggingface.co/cardiffnlp/tweet-topic-21-multi
# https://arxiv.org/abs/2209.09824

from typing import List

import itertools
from collections import Counter

import torch
from transformers import AutoTokenizer, AutoModel, AutoModelForSequenceClassification

TOK_CNFG = dict(
    padding=True,
    truncation=True,
    return_tensors="pt"
)


class TopicModel:

    def __init__(self, slug: str = 'cardiffnlp/tweet-topic-21-multi'):
        self.tokenizer = AutoTokenizer.from_pretrained(slug)
        self.model = AutoModelForSequenceClassification.from_pretrained(slug)

        self.normalize_fn = torch.nn.Sigmoid()

    def __call__(self, batch: List[str], theta: float = 0.5) -> List[List[str]]:
        logits = self.model(**self.tokenizer(batch, **TOK_CNFG)).logits

        norm_logits = (self.normalize_fn(logits) >= theta) * 1

        pred_ids = [preds.nonzero().squeeze() for preds in torch.unbind(norm_logits)]

        return [
            [self.model.config.id2label[idx] for idx in ids.tolist()]
            if type(ids.tolist()) == list else
            [self.model.config.id2label[ids.item()]]
            for ids in pred_ids
        ]


class SimilarityModel:

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
        return self.model(**self.tokenizer(batch, **TOK_CNFG)).last_hidden_state[:, 0, :]


if __name__ == '__main__':
    history = [
        'Strawberry cheesecake milkshake from the sweet spot, Virginia Beach',
        'What do you think of this yummy baklava?',
        'Death by Caramel Cheesecake for Mother\'s Day lunch.',
        'I made a velveteen rabbit red velvet cake for a friend\'s birthday'
    ]

    timeline = [
        'I made Lemon Tiramisu for Mother\'s Day dessert. Yum!',
        'Stack buttery slices of bread with prosciutto, brie and pear, then bake into a gooey, golden appetizer ✨',
        'There are still American hostages held in Gaza. Biden isn\'t focused.',
        'So disappointing another biological male stealing podium slots, medals, and financial opportunities for women in sports. This madness must stop.'
    ]

    topic_model = TopicModel()
    history_topics = topic_model(history)
    timeline_topics = topic_model(timeline)

    similarity_model = SimilarityModel()
    timeline_similarity = similarity_model(history, timeline)

    print(f'The users history includes Tweets with the topics:')
    print(Counter(list(itertools.chain(*history_topics))).most_common())
    print(f'\nThe potential timeline information:\n')

    for tweet, topic, similarity in zip(timeline, timeline_topics, timeline_similarity):
        print(f'Tweet:\t\t{tweet[:36]} [...]')
        print(f'Topic(s):\t{topic}')
        print(f'Similarity:\t{similarity}\n')
