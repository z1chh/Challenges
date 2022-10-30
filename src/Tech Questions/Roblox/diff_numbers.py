def solution(numbers):
    ct = 0
    d = {}
    s = set()
    for num in numbers:
        s.add(num)
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    s = list(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            n1 = str(s[i])
            n2 = str(s[j])
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
                    ct += d[s[i]] * d[s[j]]
    return ct
