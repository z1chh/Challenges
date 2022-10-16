def knock(s, d, fallen):
    for domino in s:
        if domino not in fallen:
            fallen.add(domino)
            if domino in d:
                knock(d[domino], d, fallen)
        

for _ in range(int(input())):
    n, m, l = map(int, input().split())
    d = dict()
    for _ in range(m):
        a, b = map(int, input().split())
        if a in d:
            d[a].add(b)
        else:
            d[a] = {b}
    fallen = set()
    for _ in range(l):
        knocked = int(input())
        knock({knocked}, d, fallen)
    print(len(fallen))
