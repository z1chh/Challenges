n = int(input())
for _ in range(n):
    s = input().lower()
    l = []
    for c in range(97, 123):
        if chr(c) not in s:
            l.append(c)
    if not l:
        print("pangram")
    else:
        print("missing {c}".format(c="".join(chr(c) for c in l)))
