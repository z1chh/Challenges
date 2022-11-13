#include <iostream>

using namespace std;

int main()
{
    int price;
    cin >> price;
    if (price < 100)
    {
        cout << 99 << endl;
        return 0;
    }

    if (price % 100 < 49)
    {
        cout << price / 100 * 100 - 1 << endl;
    }
    else
    {
        cout << price / 100 * 100 + 99 << endl;
    }
    return 0;
}
