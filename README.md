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
todo

```math
\epsilon := \text{draw random from } uniform(LOW, HIGH)
```

### Decay
todo

### Engagement
todo

### Post
todo

```python
post = Post(
    id='unique string based identifier',
    timestamp='valid datetime object',
    
    likes=[
        'list of valid datetime object',
        '...'
    ],
    
    dislikes=[
        'list of valid datetime object',
        '...'
    ],
    
    comments=[
        'list of Post object, without comments',
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
        Post(**kwargs),
        Post(**kwargs),
        Post(**kwargs),
        Post(**kwargs)
    ],
    
    reference_datetime=datetime
    
    decay=Decay(minimum=.2, reference_timedelta=datetime.timedelta(days=3))
    noise=modules.Noise(low=.6, high=1.4)
    engagement=modules.Engagement(func='count_based', log_normalize=False)
    
    weights=Weights()
)
```

### Ranker
todo
