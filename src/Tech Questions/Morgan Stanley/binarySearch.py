import math


def helper(arr, start, end, cur, n):
    if arr[cur] == n:
        return cur
    elif arr[cur] < n:
        helper(arr, start, cur, (cur - start) / 2, n)
    else:
        helper(arr, cur, end, math.floor((end - cur) / 2) + cur, n)


def solution(arr, n):
    return helper(arr, 0, len(arr), len(arr) / 2, n)


# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
#                                ^
# solution(arr, 10) -> 8 + 0
