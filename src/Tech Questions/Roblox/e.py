def solution(numbers):
    index = -1
    value = -1
    total = 0
    while True:
        for idx, num in enumerate(numbers):
            if index != -1:
                if num - value < 0:
                    break
                else:
                    numbers[idx] -= value
            else:
                if num != 0:
                    index = idx
                    value = num
                    numbers[idx] = 0
        if index == -1:
            break
        else:
            index = -1
            total += value
    return total
