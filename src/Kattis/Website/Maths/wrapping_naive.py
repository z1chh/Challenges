sawmill_area = 99.5
for _ in range(int(input())):
    boards = 0.0
    for _ in range(int(input())):
        _, _, x, y, _ = map(float, input().split())
        boards += x * y
    ans = round(boards / sawmill_area * 1000)
    print(ans / 10, "%")
