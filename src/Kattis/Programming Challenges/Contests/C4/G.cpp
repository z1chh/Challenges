#include <iostream>

using namespace std;

int main()
{
    // Initialize vars and get input
    int n, k = 1, factor = 2;
    cin >> n;

    // Loop as long as power smaller than n
    while (factor * factor <= n)
    {
        if (n % factor == 0)
        {
            n /= factor;
            k++;
        }
        else
        {
            factor++;
        }
    }

    // Output result
    cout << k;

    // Successful return
    return 0;
}
