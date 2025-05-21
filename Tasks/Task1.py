best_case = [1, 2, 3, 4, 5]
average_case = [1, 1, 2, 2, 4, 5]
worst_case = [1, 1, 1, 1, 1]


"""без set()"""
from typing import Any

def setless(nums1: list[int]):
    for k in nums1:
        if not isinstance(k, int):
            nums1 = None

    try:
        nums2 = []
        k = 0
        a = len(nums1)
        if a <= 1:
            return nums1, a
        counter = nums1[0]
        nums2.append(counter)
        for i in range(a-1):
            if nums1[i] == nums1[i+1] and nums1[i] != counter:
                nums2.append(nums1[i+1])
                counter = nums1[i+1]
            elif nums1[i] != nums1[i+1]:
                nums2.append(nums1[i+1])
                counter = nums1[i+1]
        for i in range(a - len(nums2)):
            nums2.append('_')
        for i in range(len(nums2)):
            if nums2[i] != '_':
                k += 1
        return nums2, k
    except TypeError:
        return "Cannot process this"


for _ in range(100000):
    setless(best_case)
    setless(average_case)
    setless(worst_case)


"""подсказка Алексея"""
def func(nums1: list[int]) -> str | int | Any:
    for k in nums1:
        if not isinstance(k, int):
            nums1 = None

    try:
        if len(nums1) == 1:
            return nums1, len(nums1)
        i = 0
        l = len(nums1)
        while i < l-1:
            if nums1[i] == nums1[i + 1]:
                nums1.append('_')
                nums1.pop(i)
                l -= 1
            else:
                i += 1
        return nums1, l
    except TypeError:
        return "Cannot process this"

for _ in range(100000):
    func(best_case)
    func(average_case)
    func(worst_case)