n = int(input())

for _ in range(n):
    x = int(input())
    if (x & 1):
        print("{x} is odd".format(x=x))
    else:
        print("{x} is even".format(x=x))