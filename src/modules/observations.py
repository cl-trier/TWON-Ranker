import datetime
import math
import typing

import pydantic

from src import modules


class Observations(pydantic.BaseModel):
    items: typing.List[datetime.datetime]

    def __call__(
            self,
            func: typing.Literal['count_based', 'decay_based'] = 'count_based',
            log_normalize: bool = False,
            **kwargs
    ) -> float:
        score: float = self.get_count_score() if func == 'count_based' else self.get_decayed_score(**kwargs)

        return math.log(score) if log_normalize else score

    def get_count_score(self) -> float:
        return len(self.items)

    def get_decayed_score(self, reference_datetime: datetime.datetime, decay: modules.Decay) -> float:
        return sum([decay(item, reference_datetime) for item in self.items])

    def __len__(self) -> int:
        return len(self.items)
