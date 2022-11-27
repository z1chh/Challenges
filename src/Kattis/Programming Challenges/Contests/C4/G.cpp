#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int k = 1;
    int factor = 2;
    while (factor*factor <= n)
    {
        if (n % factor == 0)
        {
            n /= factor;
            k++;
        }
        else
            factor++;
    }
    cout << k;
    return 0;
}
