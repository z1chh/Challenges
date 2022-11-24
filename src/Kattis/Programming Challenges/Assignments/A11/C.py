while (n := (int(input()))):
    n -= 1
    lst = []
    a = 1
    while n > 0:
        if n & 1:
            lst.append(a)
        a *= 3
        n >>= 1
    print("{ ", end="")
    for num in lst:
        if num == lst[0]:
            print(num, end="")
        else:
            print(f", {num}", end="")
    print(" }")
