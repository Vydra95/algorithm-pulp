import pytest
from Tasks.Task4 import palindrome

@pytest.mark.parametrize(
    "nums, res",
    [
        ("No 'x' in Nixon", True),
        ("Able was I, ere I saw Elba", True),
        ("Madam, I'm Adam", True),
        ("hello, world", False),
        ("This is not a palindrome", False),
        ("a", True),
        ("...", True),
        (12345, "Impossible to check")
    ],
)

def test_palindrome(nums, res):
    assert palindrome(nums) == res