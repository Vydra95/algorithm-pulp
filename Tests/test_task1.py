import pytest
from Tasks.Task1 import func, setless

@pytest.mark.parametrize(
    "nums, res",
    [
        ([1], ([1], 1)),
        ([1, 1, 2], ([1, 2, '_'], 2)),
        ([7, 7, 7, 7, 7, 7, 7], ([7, '_', '_', '_', '_', '_', '_'], 1)),
        ([], ([], 0)),
        (['a', 'b', 'b'], "Cannot process this")

    ],
)

def test_func(nums, res):
    assert func(nums) == res

@pytest.mark.parametrize(
    "nums, res",
    [
        ([1], ([1], 1)),
        ([1, 1, 2], ([1, 2, '_'], 2)),
        ([7, 7, 7, 7, 7, 7, 7], ([7, '_', '_', '_', '_', '_', '_'], 1)),
        ([], ([], 0)),
        (['a', 'b', 'b'], "Cannot process this")

    ],
)

def test_setless(nums, res):
    assert setless(nums) == res
