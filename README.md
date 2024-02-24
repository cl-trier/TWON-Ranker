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
todo

### Noise
Draw random floating point numbers from the normal distribution provided lower and upper boundaries.

```math
\epsilon := \text{draw random from } uniform(LOW, HIGH)
```

```python
LOW: float
HIGH: float

eps = modules.Noise(low=LOW, high=HIGH)

rnd_number: float = eps()
rnd_samples: List[float] = eps.draw_samples(N)
```

### Decay
todo

```python
MINIMUM: float
REFERENCE_TIMEDELTA: datetime.timedelta

decay = modules.Decay(minimum=MINIMUM, reference_timedelta=REFERENCE_TIMEDELTA)

# todo
```

### Engagement
todo

```python
FUNC: Literal['count_based', 'decay_based']
LOG_NORMALIZE: bool

E = modules.Engagement(func=FUNC, log_normalize=LOG_NORMALIZE)

# todo
```

## Usage

### Post
todo

```python
post = Post(
    id='unique string based identifier',
    timestamp='valid datetime object',
    
    likes=[
        'list of valid datetime objects',
        '...'
    ],
    
    dislikes=[
        'list of valid datetime objects',
        '...'
    ],
    
    comments=[
        'list of Post objects, without comments',
        '...'
    ]
)
```

### Weights
todo

```python
w = Weights(
    likes=1.
    dislikes=1.
    comments=1.

    comments_likes=1.
    comments_dislikes=1.
)
```

### Request
todo

```python
req = Request(
    items=[
        'list of Post objects', # see Usage:Post
        '...'
    ],
    
    reference_datetime='valid datetime object'
    
    decay=modules.Decay(minimum=.2, reference_timedelta=datetime.timedelta(days=3))
    noise=modules.Noise # see Modules:Noise
    engagement=modules.Engagement(func='count_based', log_normalize=False)
    
    weights=Weights  # see Usage:Weights
)
```

### Ranker
todo
