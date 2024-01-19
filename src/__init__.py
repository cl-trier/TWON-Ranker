from typing import List, Dict, Tuple

import transformers

from .modules import SimilarityComputer, TopicClassifier, NetworkAnalysis
from .schemas import User, Post
from .schemas.shared import RankingMap, FeatureTable

transformers.logging.set_verbosity_error()


class Recommender:

    def __init__(self):
        self.modules = dict(
            similarity=SimilarityComputer(),
            topic=TopicClassifier(),
            **NetworkAnalysis().features_map
        )

    def __call__(
            self,
            user: User,
            posts: List[Post],
            weights: Dict[str, float]
    ) -> Tuple[RankingMap, FeatureTable]:
        features: FeatureTable = {post.id: dict() for post in posts}

        for module in self.modules.keys():
            self.apply_module(features, module, user, posts)

        return self.compute_weighted_ranking(features, weights), features

    def apply_module(
            self,
            features: FeatureTable,
            module_name: str,
            user: User,
            posts: List[Post]
    ) -> None:
        for pid, value in self.modules[module_name](user, posts).items():
            features[pid][module_name] = value

    @staticmethod
    def compute_weighted_ranking(features: FeatureTable, weights: Dict[str, float]) -> RankingMap:
        return {
            pid: sum([value * weights.get(key, 1.) for key, value in feature.items()])
            for pid, feature in features.items()
        }
