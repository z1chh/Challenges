#include <iostream>

using namespace std;

int main()
{
    int numBreaks, breakPrice, bestProfit, tmp, startIndex, size, curProfit;

    // Get input
    cin >> numBreaks;
    cin >> breakPrice;

    int studentsPerBreak[numBreaks];
    for (int i = 0; i < numBreaks; i++)
    {
        cin >> studentsPerBreak[i];
    }

    // Find best sequence
    bestProfit = -1;
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