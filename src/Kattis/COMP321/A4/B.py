while True:
    try:
        l = list(map(int, input().split()))
    except:
        break
    rocks = l[0]
    nm = l[1]
    moves = l[2:]
    l = [False] * (rocks + 1)
    for i in range(1, rocks + 1):
        for move in moves:
            if i - move >= 0 and not l[i - move]:
                l[i] = True
                break
            
    print("Stan wins" if l[rocks] else "Ollie wins")
