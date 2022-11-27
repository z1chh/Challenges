# For each test case
for case in range(1, int(input()) + 1):
    # Ignore
    input()

    # Initialize empty set
    count = set()

    # Loop through input
    for p in map(int, input().split()):
        if p in count:
            count.remove(p)
        else:
            count.add(p)

    # Output result
    print("Case #" + str(case) + ": " + str(count.pop()))
