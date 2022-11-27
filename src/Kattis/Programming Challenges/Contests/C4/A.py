import math


# Get your location
cx, cy, n = map(int, input().split())

# Get listeners
radius = []
for i in range(n):
    x, y, r = map(int, input().split())
    d = math.pow(math.pow((cx - x), 2) + math.pow((cy - y), 2), 0.5) - r
    radius.append(d)

# Sort
radius.sort()

# Output third
print(math.floor(radius[2]) if radius[2] > 0 else 0)
