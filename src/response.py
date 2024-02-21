import datetime
import json
import uuid

import pydantic

from src import request
from src.model import shared


class Response(pydantic.BaseModel):
    id: uuid.UUID = None
    timestamp: datetime.datetime = None

    request: request.Request
    ranking_map: shared.Ranking

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
