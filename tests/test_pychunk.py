import pytest
from pychunk import chunk

data = [
    # param with num_chunks
    ([1, 2, 3, 4, 5], {"num_chunks": 0}, [[1, 2, 3, 4, 5]]),          #l0
    ([1, 2, 3, 4, 5], {"num_chunks": 1}, [[1, 2, 3, 4, 5]]),          #l1
    ([1, 2, 3, 4, 5], {"num_chunks": 2}, [[1, 2, 3], [4, 5]]),        #l2 
    ([1, 2, 3, 4, 5], {"num_chunks": 3}, [[1, 2], [3, 4], [5]]),      #l3
    ([1, 2, 3, 4, 5], {"num_chunks": 10}, [[1], [2], [3], [4], [5]]), #l4
    
    # param with num_items in each chunk
    ([1, 2, 3, 4, 5], {"num_items": 0}, [[1, 2, 3, 4, 5]]),         #l5
    ([1, 2, 3, 4, 5], {"num_items": 1}, [[1], [2], [3], [4], [5]]), #l6
    ([1, 2, 3, 4, 5], {"num_items": 2}, [[1, 2], [3, 4], [5]]),     #l7
    ([1, 2, 3, 4, 5], {"num_items": 3}, [[1, 2, 3], [4, 5]]),       #l8
    ([1, 2, 3, 4, 5], {"num_items": 10}, [[1, 2, 3, 4, 5]]),        #l9
]


@pytest.mark.parametrize("l, params, expected", data)
def test_chunk_with_different_params(l, params, expected):
    output = list(chunk(l=l, **params))
    assert output == expected
