def solution(numbers):
    ct = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            n1 = str(numbers[i])
            n2 = str(numbers[j])
            if len(n1) != len(n2):
                continue
            else:
                diff = 0
                for c1, c2 in zip(n1, n2):
                    if c1 != c2:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    ct += 1
    return ct
