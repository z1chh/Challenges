#include <iostream>

using namespace std;

int main()
{
    // Get number of squares
    int destination;
    cin >> destination;

    // Get cost per square
    int prices[destination];
    for (int i = 0; i < destination; i++)
    {
        cin >> prices[i];
    }

    // Initialize dp matrix with values = -1
    int dp[destination + 1][destination + 1];
    for (int i = 0; i < destination + 1; i++)
    {
        for (int j = 0; j < destination + 1; j++)
        {
            dp[i][j] = -1;
        }
    }

    // DP backwards
    int step, square, forward, backward, value;
    for (step = destination; step >= 0; step--)
    {
        for (square = 1; square < destination + 1; square++)
        {
            forward = square + step + 1;
            backward = square - step;

            // Check if square is destination
            if (square == destination)
            {
                dp[step][square] = prices[destination - 1];
            }
            
            // Check if we can move forward
            if (forward <= destination && step < destination)
            {
                if (dp[step + 1][forward] != -1)
                {
                    dp[step][square] = dp[step + 1][forward] + prices[square - 1];
                }
            }

            // Check if we can move backward
            if (backward > 0)
            {
                if (dp[step][backward] != -1)
                {
                    value = dp[step][backward] + prices[square - 1];
                    if (dp[step][square] == -1 || value < dp[step][square])
                    {
                        dp[step][square] = value;
                    }
                }
            }
        }
    }

    // Output results
    cout << dp[1][2] << endl;

    // Successful exit
    return 0;
}
