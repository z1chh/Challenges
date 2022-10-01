# Get input
input()  # Don't care
l = list(map(int, input().split()))

# Sort l in reverse order (trees that take the longest to grow)
l.sort(reverse=True)

# Longest day, set to -1
t = -1

# Search for longest day
for i, d in enumerate(l):
    # Longest day is start day + time it takes to fully grow
    if i + 1 + d > t:  # (i + 1) since days start at 1, not 0
        t = i + 1 + d

# Output the results
print(t + 1)  # t + 1 since the party starts the next day only
