# Get input
ns, cap, dif = map(int, input().split())
socks = list(map(int, input().split()))

# Sort socks in color order
socks.sort()

b = 0
while socks:
    c1 = socks[0]  # First color
    socks.pop(0)  # Create new batch to wash
    cc = 1  # Number of socks currently in the batch
    while cc < cap and socks:
        if socks[0] - c1 <= dif:
            socks.pop(0)
            cc += 1
        else:
            break

    # Increment number of batches
    b += 1

# Output results
print(b)
