"""максимальный элемент в целочисленном
списке nums, который встречается минимум n / 2 раз"""

def findnum (nums):
    for k in nums:
        if not isinstance(k, int):
            nums = None
    try:
        n = len(nums) / 2
        adict = {}
        for i in range (len(nums)):
            if nums[i] in adict:
                adict[nums[i]] += 1
            else:
                adict[nums[i]] = 1
        lmax = 0
        count = 0
        for key, value in adict.items():
            if value >= n and key >= lmax:
                lmax = key
                count += 1
        if count > 0:
            return lmax
        else:
            return None
    except TypeError:
        return "Can't process that"

print(findnum(nums))
