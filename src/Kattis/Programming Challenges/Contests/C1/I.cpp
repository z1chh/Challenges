#include <iostream>

using namespace std;

int main()
{
    int e, f, c, total, to_return = 0;
    cin >> e >> f >> c;
    total = e + f;
    while (total >= c)
    {
        total -= (c - 1);
        to_return += 1;
    }
    cout << to_return << endl;
    return 0;
}
