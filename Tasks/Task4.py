best_case = "Abba"
average_case = "A man, a plan, a canal: Panama"
worst_case = "abcdefghijklmnopqrstuvwxyz"

"""Решение изначальное"""
def palindrome(s):
    try:
        if s == "":
            raise AttributeError
        s = s.lower()
        s = ''.join(char for char in s if char in "abcdefghijklmnopqrstuvwxyz")
        res = True
        for i in range (len(s) - 1):
            if s[i] != s[(len(s) - 1) - i]:
                res = False
        return res
    except AttributeError:
        return "Impossible to check"

for _ in range(100000):
    palindrome(best_case)
    palindrome(average_case)
    palindrome(worst_case)


"""Решение обратным срезом (вроде бы)"""
def palindrome_cut(s):
    try:
        if s == "":
            raise AttributeError
        s = s.lower()
        s = ''.join(char for char in s if char in "abcdefghijklmnopqrstuvwxyz")
        return s == s[::-1]
    except AttributeError:
        return "Impossible to check"

for _ in range(100000):
    palindrome_cut(best_case)
    palindrome_cut(average_case)
    palindrome_cut(worst_case)


"""Решение методом двух указателей"""
def palindrome_double(s):
    left, right = 0, len(s) - 1
    possible = "abcdefghijklmnopqrstuvwxyz"
    while left < right:
        while left < right and not s[left].lower() in possible:
            left += 1
        while left < right and not s[right].lower() in possible:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

for _ in range(100000):
    palindrome_double(best_case)
    palindrome_double(average_case)
    palindrome_double(worst_case)
