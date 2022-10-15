# Get input
dest = int(input())
prices = [int(input()) for _ in range(dest)]
dp = [[-1] * (dest + 1) for _ in range(dest + 1)] # Dynamic programming matrix

# Start from the end
for step in range(dest, -1, -1):
    for square in range (1, dest + 1):
        if square == dest:
            dp[step][square] = prices[-1]
            continue
        square_forward = square + step + 1
        square_backward = square - step
        if square_forward <= dest and step < dest:
            if dp[step + 1][square_forward] != -1:
                dp[step][square] = dp[step + 1][square_forward] + prices[square - 1]
        if square_backward > 0:
            if dp[step][square_backward] != -1:
                value = dp[step][square_backward] + prices[square - 1]
                if dp[step][square] == -1 or value < dp[step][square]:
                    dp[step][square] = value
print(dp[1][2])
