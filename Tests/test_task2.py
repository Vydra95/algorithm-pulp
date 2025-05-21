import pytest
from Tasks.Task2 import delete_doubles, obliterate_doubles


@pytest.mark.parametrize(
    "nums, res",
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]),
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
        ([7, 7, 7, 7, 7], [7, 7]),
        ([], []),
        ([5], [5]),
        ([0, 0], [0, 0]),
        ([1, 1, 1, 2, 2, 2, 2, 3, 3, 4], [1, 1, 2, 2, 3, 3, 4]),
        ([-2, -2, -1, -1, 0, 0, 0, 1, 1], [-2, -2, -1, -1, 0, 0, 1, 1]),
        (['a', 'b', 'c'], "Can't process that"),
    ],
)

def test_delete_doubles(nums, res):
    assert delete_doubles(nums) == res

@pytest.mark.parametrize(
    "nums, res",
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]),
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
        ([7, 7, 7, 7, 7], [7, 7]),
        ([], []),
        ([5], [5]),
        ([0, 0], [0, 0]),
        ([1, 1, 1, 2, 2, 2, 2, 3, 3, 4], [1, 1, 2, 2, 3, 3, 4]),
        ([-2, -2, -1, -1, 0, 0, 0, 1, 1], [-2, -2, -1, -1, 0, 0, 1, 1]),
        (['a', 'b', 'c'], "Can't process that"),
    ],
)

def test_obliterate_doubles(nums, res):
    assert obliterate_doubles(nums) == res