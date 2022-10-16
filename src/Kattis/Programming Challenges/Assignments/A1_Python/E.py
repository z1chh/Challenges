for _ in range(int(input())):
    s = input().lower()
    l = []
    for c in range(97, 123):
        if chr(c) not in s:
            l.append(c)
    print("pangram" if not l else "missing {c}".format(c="".join(chr(c) for c in l)))
