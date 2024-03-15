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
The purpose of the decay object is to compute a decay factor based on time differences. In the context of this project, the decay factor is used, for instance, to decrease the relevance of posts over time, so that older posts move to occupy lower positions in the ranking.
We instantiate a decay object by defining a minimum value, which is going to serve as a lower boundary for the decay, as well as a reference time interval. When called, the decay object calculates a time difference between the reference time interval and the observed time interval . This value is then subtracted from 1, and the decay factor resulting from this operation is returned, accordingly. 


```python
from src.modules import Decay

MINIMUM: float
REFERENCE_TIMEDELTA: timedelta

decay = Decay(minimum=MINIMUM, reference_timedelta=REFERENCE_TIMEDELTA)

# todo
```

### Engagement
The object E is an instance of the Engagement class, which is designed to compute engagement scores based on different criteria. The func attribute can be either ‘count_based’ or or ‘decay_based’. If the former is selected, then the engagement score is calculated by simply counting the items, whereas, if the latter is selected, the engagement score is obtained by applying decay to each item and then summing the items together. Moreover, the log_normalize attribute defines whether or not to return a natural logarithm of the score.

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
We want to create an object to represent a social media post, therefore, we instantiate it from the Post class. To do so, we firstly define the following variables:
- **ID**: A placeholder variable for the unique identifier (ID) of the post (string).
- TIMESTAMP: A placeholder variable for the timestamp when the post was created. This is a datetime object, i.e. an object that combines date and time information. 
- **OBSERVATIONS**: A placeholder variable for a list of observations (timestamps, see above). Notice that upon creating the post object, these timestamps represent both likes and dislikes.
- **COMMENTS**: A placeholder variable for a list of Post objects representing comments 


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
We create a Request object with the specified parameters to perform a range of computations related to engagement. The weights attribute contains several knobs that can be tweaked to affect the different engagement factors (here, we provided some default values for likes, dislikes, comments, etc.)
The request object makes use of the weights attribute, as well as the following attributes:
- **items**: a list of Post objects 
- **reference_datetime**: takes a datetime object, i.e. an object that combines date and time information. 
- **decay**: takes the decay factor 
- **noise**: takes the noise factor
- **engagement**: takes the engagement factor

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
