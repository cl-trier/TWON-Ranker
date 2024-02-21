import datetime

import pydantic


class Decay(pydantic.BaseModel):
    # todo: find a better variable name
    minimum: float = 0.2
    interval: datetime.timedelta = datetime.timedelta(days=3)

    def __call__(
            self,
            observation_time: datetime.datetime,
            current_time: datetime.datetime
    ) -> float:
        decay: float = 1. - (
                (current_time - observation_time).total_seconds()
                / self.interval.total_seconds()
        )

        return (
            decay
            if decay >= self.minimum else
            self.minimum
        )
