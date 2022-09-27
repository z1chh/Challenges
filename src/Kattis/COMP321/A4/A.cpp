#include <iostream>

using namespace std;

int main()
{
    // Variables
    int num_breaks, break_price, profit, best_profit = -1;

    // Get input
    cin >> num_breaks;
    cin >> break_price;

    // Get the price per break
    int price_per_break[num_breaks];
    for (int i = 0; i < num_breaks; i++)
    {
        cin >> profit;
        profit -= break_price;
        price_per_break[i] = profit;
        if (profit > best_profit)
        {
            best_profit = profit;
        }
    }

    // Initialize DP array
    int dp[num_breaks - 1];
    for (int i = 0; i < num_breaks - 1; i++)
    {
        profit = price_per_break[i] + price_per_break[i + 1];
        dp[i] = profit;
        if (profit > best_profit)
        {
            best_profit = profit;
        }
    }

    for (int i = 3; i <= num_breaks; i++)
    {
        for (int j = 0; j <= num_breaks - i; j++)
        {
            profit = dp[j] + price_per_break[i + j - 1];
            dp[j] = profit;
            if (profit > best_profit)
            {
                best_profit = profit;
            }
        }
    }

    // Output result
    cout << best_profit << endl;

    // Successful return code
    return 0;
}
