#include <iostream>

using namespace std;

int main()
{
    // Variables
    int numBreaks, breakPrice, profit, bestProfit = -1, startIndex, size, curProfit;

    // Get input
    cin >> numBreaks;
    cin >> breakPrice;

    // Get students per break
    int studentsPerBreak[numBreaks];
    for (int i = 0; i < numBreaks; i++)
    {
        cin >> studentsPerBreak[i];
    }

    // Find best sequence
    int pricePerBreak[numBreaks];
    for (int i = 0; i < numBreaks; i++)
    {
        pricePerBreak[i] = studentsPerBreak[i] - breakPrice;
    }

    for (int i = 0; i < numBreaks; i++)
    {
        for (int j = i; j < numBreaks; j++)
        {
            startIndex = j;
            size = i;
            curProfit = 0;
            while (size-- >= 0)
            {
                curProfit += pricePerBreak[startIndex--];
            }
            if (curProfit > bestProfit)
            {
                bestProfit = curProfit;
            }
        }
    }

    cout << bestProfit << endl;
    return 0;
}