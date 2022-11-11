import math


for _ in range(int(input())):
    s = input()
    l = int(math.sqrt(len(s)))
    m = []
    for i in range(l):
        ss = ""
        for j in range(l):
            ss += s[i * l + j]
        m.append(ss[::-1])
    tr = ""
    for i in range(l):
        for j in range(l):
            tr += m[j][i]
    print(tr)
