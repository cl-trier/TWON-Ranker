from typing import List, Dict

import transformers

from src import modules
from src import schemas
from src.response import Response

transformers.logging.set_verbosity_error()


class Ranker:

    def __init__(self, log_path: str = None):
        self.log_path = log_path

        self.modules = dict(
            similarity=modules.SimilarityComputer(),
            topic=modules.TopicClassifier(),
            **modules.NetworkAnalysis().features_map
        )

    def __call__(
            self,
            user: schemas.User,
            posts: List[schemas.Post],
            weights: Dict[str, float]
    ) -> Response:
        """
        Calculate the ranking and feature table based on user, posts, and weights.
        Args:
            user (User): The user object representing the user.
            posts (List[Post]): A list of Post objects representing the posts.
            weights (Dict[str, float]): A dictionary mapping feature names to weights.

        Returns:
            Response: A tuple containing the ranking map and feature table.
        """
        features: schemas.shared.FeatureTable = {post.id: dict() for post in posts}

        for module in self.modules.keys():
            self.apply_module(features, module, user, posts)

        return Response(
            ranking_map=self.compute_weighted_ranking(features, weights),
            feature_table=features,
            user=user,
            posts=posts,
            log_path=self.log_path
        )

    def apply_module(
            self,
            features: schemas.shared.FeatureTable,
            module_name: str,
            user: schemas.User,
            posts: List[schemas.Post]
    ) -> None:
        """
        Apply a specified module to the given features.

        Args:
            features (FeatureTable): The feature table to apply the module to.
            module_name (str): The name of the module to apply.
            user (User): The user object.
            posts (List[Post]): The list of posts.

        Returns:
            None: This function does not return anything.
        """
        for pid, value in self.modules[module_name](user, posts).items():
            features[pid][module_name] = value

    @staticmethod
    def compute_weighted_ranking(
            features: schemas.shared.FeatureTable,
            weights: Dict[str, float]
    ) -> schemas.shared.RankingMap:
        """
        Compute the weighted ranking for a given set of features.
        Args:
            features (FeatureTable): A dictionary containing the features for each pid.
            weights (Dict[str, float]): A dictionary containing the weights for each feature.
        Returns:
            RankingMap: A dictionary mapping each pid to its computed weighted ranking.
        """
        return {
            pid: sum([value * weights.get(key, 1.) for key, value in feature.items()])
            for pid, feature in features.items()
        }
