def shift(arr):
    return arr[1:] + [arr[0]]


def getAbsDiffs(arr1, arr2):
    to_return = 0
    for n1, n2 in zip(arr1, arr2):
        to_return += abs(n1 - n2)
    return to_return


def solution(arr1, arr2):
    sums = []
    for _ in range(len(arr1)):
        sums.append(getAbsDiffs(arr1, arr2))
        arr1 = shift(arr1)
    return min(sums)
