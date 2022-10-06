for _ in range(int(input())):
    s1 = input()
    s2 = input()
    tr = []
    for c1, c2 in zip(s1, s2):
        tr.append("*" if c1 != c2 else ".")
    print(s1)
    print(s2)
    print("".join(tr))
