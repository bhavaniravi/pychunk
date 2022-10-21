# PyChunk

A Python library to chunk list based on number of items or number of chunks

## Why?

Two Reasons!

1. Python doesn't come with out of box chunking functionality for lists. Hence I thought of writing a library instead of referring stackoverflow everytime
2. I always wanted to publish a library in pypi

## Installation

```
pip install pychunk
```
## Usage

```python
from pychunk import chunk

chunk([1, 2, 3, 4, 5], num_chunks=2)
chunk([1, 2, 3, 4, 5], num_items=3)
```

## Tech Used

1. Peotry for package management
2. Pytest for testing
3. Mypy for static code checking

> This is my first time using python types in my project

## Ahaa moments!

1. I'm deeply suprised by how Poetry makes it so simple to publish a library. I always got list in setuptools and disttools
2. But, I don't think poetry supports `pip install -e .` [equivalent command](https://github.com/python-poetry/poetry/issues/34)
3. Looks like it's been added to [Poetry 1.2](https://github.com/python-poetry/poetry/issues/34#issuecomment-1193365526). Need to figure out how it works. 