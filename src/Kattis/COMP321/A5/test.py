def t1():
    l = [1, 5, 3, 12, 2, 7]
    l2 = l.copy()
    print(l)
    print(l2)
    l2.sort(reverse=True)
    print(l)
    print(l2)
    print(l2.index(12))
    l2.remove(1)
    print(l2)


def t2():
    l = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    print(l)


t2()
