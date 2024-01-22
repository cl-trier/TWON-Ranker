from typing import Dict

Post_ID = str
Author_ID = str

RankingMap = Dict[Post_ID, float]
FeatureTable = Dict[Post_ID, Dict[str, float]]
