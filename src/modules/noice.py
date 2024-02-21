import random

import pydantic


class Noice(pydantic.BaseModel):
    min: float = 0.8
    max: float = 1.4

    def __call__(self):
        return random.uniform(self.min, self.max)

