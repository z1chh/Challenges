import math
for _ in range(int(input())):
    radius, people, angle, minutes, seconds = map(int, input().split())
    area = math.pow(math.pi, 2) * radius
    print("pi and area:", math.pi, area)
    print(area * angle / 360.)
