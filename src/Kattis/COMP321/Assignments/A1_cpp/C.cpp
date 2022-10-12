#include <iostream>

using namespace std;

int main()
{
    int nc, v, i, neg = 0;
    cin >> nc;
    for (i = 0; i < nc; i++)
    {
        cin >> v;
        if (v < 0)
        {
            neg++;
        }
    }
    cout << neg << endl;
    return 0;
}
