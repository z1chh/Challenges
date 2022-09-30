dogs = list(map(int, input().split()))
t1 = dogs[0] + dogs[1]
t2 = dogs[2] + dogs[3]
for t in list(map(int, input().split())):
    d1 = True
    d2 = True
    if t % t1 > dogs[0] or t % t1 == 0:
        d1 = False
    if t % t2 > dogs[2] or t % t2 == 0:
        d2 = False
    if d1 and d2:
        print("both")
    elif not d1 and not d2:
        print("none")
    else:
        print("one")
