def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    print(abs(x1 - x2) * abs(y1 - y2))
    return abs(x1 - x2) * abs(y1 - y2)


# For each test case
for _ in range(int(input())):
    # Get number of possible spots for watchtowers
    num_spots = int(input())

    # Get each potential location
    spots = []
    for _ in range(num_spots):
        x, y = map(int, input().split())
        spots.append((x, y))

    # Exhaustive search
    biggest = 0
    for i in range(num_spots - 1):
        for j in range(i + 1, num_spots):
            if (cur := area(spots[i], spots[j])) > biggest:
                biggest = cur

    # Output biggest area
    print(biggest)
