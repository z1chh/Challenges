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
    for (int step = destination; step >= 0; step--)
    {
        for (int square = 1; square < destination + 1; square++)
        {
            // TODO
        }
    }
}
