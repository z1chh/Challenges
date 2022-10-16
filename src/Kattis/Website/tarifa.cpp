#include <iostream>

using namespace std;

int main()
{
    int x, n, p, tr;
    cin >> x >> n;
    tr = x * (n + 1);
    for (int i = 0; i < n; i++)
    {
        cin >> p;
        tr -= p;
    }
    cout << tr << endl;
    return 0;
}
