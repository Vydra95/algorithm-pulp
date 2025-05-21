best_case = [1, 1, 2, 2, 3, 3]
average_case = [1, 2, 2, 3, 3, 3]
worst_case = [1, 1, 1, 1, 1, 1, 1]


"""Со словарём"""
def delete_doubles(nums: list[int]) -> list[int] | str:
    for k in nums:
        if not isinstance(k, int):
            nums = None
    try:
        dct = {}
        for n in nums:
            if n not in dct:
                dct[n] = 0
            dct[n]+= 1
        nums = []
        for i in dct:
            if dct[i] == 1:
                nums.append(i)
            if dct[i] >= 2:
                nums.append(i)
                nums.append(i)
        return nums
    except TypeError:
        return "Can't process that"

for _ in range(100000):
    delete_doubles(best_case)
    delete_doubles(average_case)
    delete_doubles(worst_case)


"""Без словаря"""
def obliterate_doubles(nums: list[int]) -> list[int] | str:
    for k in nums:
        if not isinstance(k, int):
            nums = None
    try:
        i = len(nums) - 1
        while i > 1:
            if nums[i] == nums[i - 1]:
                if nums[i - 1] == nums[i - 2]:
                    nums.remove(nums[i - 1])
            i -= 1
        return nums
    except TypeError:
        return "Can't process that"

for _ in range(100000):
    obliterate_doubles(best_case)
    obliterate_doubles(average_case)
    obliterate_doubles(worst_case)