import datetime
import typing

import pydantic

import modules


class Observations(pydantic.BaseModel):
    items: typing.List[datetime.datetime]

    def get_score(self):
        return len(self.items)

    def get_decayed_score(self, now: datetime.datetime, decay: modules.Decay):
        return sum([decay(item, now) for item in self.items])
