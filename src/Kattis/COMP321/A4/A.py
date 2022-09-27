# Main function
def radio_commercials():
    # Get input
    num_breaks, break_price = list(map(int, input().split()))
    price_per_break = list(map(int, input().split()))

    best_profit = -1

    for i in range(num_breaks):
        profit = price_per_break[i] - break_price
        price_per_break[i] = profit
        if profit > best_profit:
            best_profit = profit

    # Create new DP array
    dp = []

    # Initialize first row
    for i in range(num_breaks - 1):
        profit = price_per_break[i] + price_per_break[i + 1]
        dp.append(profit)
        if profit > best_profit:
            best_profit = profit

    # Compute for sequences of breaks
    for i in range(3, num_breaks + 1):
        for j in range(0, num_breaks - i + 1):
            profit = dp[j] + price_per_break[i + j - 1]
            dp[j] = profit
            if profit > best_profit:
                best_profit = profit

    # Output profit
    print(best_profit)


# Main
if __name__ == "__main__":
    radio_commercials()
