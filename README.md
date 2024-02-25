# TWON: Ranker - Modularized & Weighted Timeline Ranking
todo

## Project Setup
todo

```sh
# install Python requirements
make install

# start api with hot-reload for development
make dev

# start api for production
make serve

# run unit tests
make test
```

## Modules
The current TWON ranking/recommendation algorithm is divided into three encapsulated modules that composed denote the ranking function. These modules provide the functionalities to measure engagement given a predefined data format, represent the course of time, and partly randomize the final ranking.

### Noise
We draw random floating point numbers from the normal distribution provided lower and upper boundaries to generate a multiplicative noise (the neutral value defined as `LOW = HIGH = 1.` will result in no noise).

```python
from src.modules import Noise

LOW: float
HIGH: float
N: int

eps = Noise(low=LOW, high=HIGH)

rnd_number: float = eps()
rnd_samples: List[float] = eps.draw_samples(N)
```

### Decay
todo

```python
from src.modules import Decay

MINIMUM: float
REFERENCE_TIMEDELTA: timedelta

decay = Decay(minimum=MINIMUM, reference_timedelta=REFERENCE_TIMEDELTA)

# todo
```

### Engagement
todo

```python
from src.modules import Engagement

FUNC: Literal['count_based', 'decay_based']
LOG_NORMALIZE: bool

E = Engagement(func=FUNC, log_normalize=LOG_NORMALIZE)

# todo
```

## Usage
todo

### Post
todo

```python
from src.post import Post

ID: str
TIMESTAMP: datetime
OBERSERVATIONS: List[datetime]
COMMENTS: List[Post] # post objects w/o comments

post = Post(
    id=ID,
    timestamp=TIMESTAMP,
    likes=OBERSERVATIONS,
    dislikes=OBERSERVATIONS,
    comments=COMMENTS,
)

# todo
```

### Request
todo

```python
from src.request import Request, Weights

ITEMS: List[Post] # see Usage:Post
REFERENCE_DATETIME: datetime
DECAY: modules.Decay  # see Modules:Decay
NOISE: modules.Noise  # see Modules:Noise
ENGAGEMENT: modules.Engagement # see Modules:Engagement

WEIGHTS: Weights(
    likes=1.
    dislikes=1.
    comments=1.

    comments_likes=1.
    comments_dislikes=1.
)

req = Request(
    items=ITEMS,
    reference_datetime=REFERENCE_DATETIME,
    decay=DECAY,
    noise=NOISE,
    engagement=ENGAGEMENT
    weights=WEIGHTS
)
```

### Ranker
todo

```python
# todo
```
