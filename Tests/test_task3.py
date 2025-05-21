import pytest
from Tasks.Task3 import findnum

@pytest.mark.parametrize(
    "nums, res",
    [
        ([5], 5),
        ([3, 3, 3, 3], 3),
        ([2, 2, 1, 2, 2], 2),
        ([4, 4, 5, 5, 5], 5),
        ([6, 6, 6, 7], 6),
        ([-1, -1, -2, -2, -2], None),
        ([1, 2, 3, 4], None),
        ([], None),
        ([8, 8, 9, 9], 9),
        (['a', 'b', 'c'], "Can't process that"),
    ],
)

def test_findnum(nums, res):
    assert findnum(nums) == res