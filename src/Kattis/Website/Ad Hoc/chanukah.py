for _ in range(int(input())):
    i, d = list(map(int, input().split()))
    candles = d
    for c in range(1, d + 1):
        candles += c
    
    print(i, candles)
    