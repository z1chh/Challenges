#include <iostream>

using namespace std;

int getAllBaskets(int *fruitWeights, int numFruits)
{
    int allBaskets = 0, curWeight, ct = numFruits - 1, c;

    int arr[numFruits];
    for (int i = 0; i < numFruits; i++)
    {
        arr[i] = 0;
    }

    while (true)
    {
        if (arr[ct] == 0)
        {
            arr[ct] = 1;
        }
        else
        {
            int c = 1;
            while (ct - c >= 0)
                if (arr[ct - c] == 0)
                {
                    arr[ct - c] = 1;
                    for (int i = ct - c + 1; i < numFruits; i++)
                    {
                        arr[i] = 0;
                    }
                    break;
                }
                else
                {
                    c++;
                }
            if (ct - c < 0)
                break;
        }

        curWeight = 0;
        for (int i = 0; i < numFruits; i++)
        {
            if (arr[i] == 1)
            {
                curWeight += fruitWeights[i];
            }
        }

        if (curWeight >= 200)
        {
            allBaskets += curWeight;
        }
    }
    return allBaskets;
}

int main()
{
    int numFruits;
    cin >> numFruits;

    int fruitWeights[numFruits];
    for (int i = 0; i < numFruits; i++)
    {
        cin >> fruitWeights[i];
    }

    cout << getAllBaskets(fruitWeights, numFruits) << endl;
    return 0;
}