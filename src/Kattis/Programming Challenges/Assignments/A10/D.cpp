#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Get input
    string inp;
    long long zeros = 0, ones = 0, twos = 0, swaps = 0;
    cin >> inp;

    // For each kid
    for (char c: inp)
    {
        if (c == '0')
        {
            zeros++;
            swaps += ones + twos;
        }
        else if (c == '1')
        {
            ones++;
            swaps += twos;
        }
        else
        {
            twos++;
        }
    }

    // Output minimum number of swaps
    cout << swaps << endl;

    // Successful return
    return 0;
}
