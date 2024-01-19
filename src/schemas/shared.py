from typing import Dict

Post_ID = int
Author_ID = int

RankingMap = Dict[Post_ID, float]
FeatureTable = Dict[Post_ID, Dict[str, float]]
