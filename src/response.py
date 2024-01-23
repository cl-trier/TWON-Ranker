import datetime
import json
import uuid
from typing import List

from pydantic import BaseModel

from src import schemas


class Response(BaseModel):
    id: uuid.UUID = None
    timestamp: datetime.datetime = None
    
    user: schemas.User
    posts: List[schemas.Post]

    ranking_map: schemas.shared.RankingMap
    feature_table: schemas.shared.FeatureTable

    def __init__(self, log_path: str = None, **data):
        super().__init__(**data)

        self.id = uuid.uuid1()
        self.timestamp = datetime.datetime.now()

        if log_path:
            self.log(log_path)

    def log(self, path: str) -> None:
        json.dump(
            self.model_dump(mode='json', exclude=set('log_path')),
            open(f'{path}/{self.id}.json', "w"),
            indent=4
        )
