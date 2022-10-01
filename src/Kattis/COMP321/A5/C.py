# Get input
num_socks, cap, dif = map(int, input().split())
ss = list(map(int, input().split()))
ss.sort()

# Sort socks in order by color
socks = {}
for s in ss:
    if s in socks.keys():
        socks[s] += 1
    else:
        socks[s] = 1

num_batches = 0
#print("socks to wash:", socks)
while num_socks > 0:
    # Start a batch
    num_batches += 1
    
    # Reset vars
    current_socks = 0
    color_diff_reached = False
    first_color = -1

    # Get socks for the current batch
    while current_socks < cap and num_socks > 0 and not color_diff_reached:
        for color in socks.keys():
            if socks[color] > 0:
                if first_color == -1:
                    first_color = color
                elif color - first_color > dif:
                    color_diff_reached = True
                    break
                to_add = min(socks[color], cap - current_socks)
                socks[color] -= to_add
                current_socks += to_add
                num_socks -= to_add
    #print("socks to wash:", socks)

# Output results
print(num_batches)
