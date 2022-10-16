#include <iostream>

using namespace std;

int main()
{
    int g, s, c, p;
    cin >> g >> s >> c;
    p = 3 * g + 2 * s + c;
    if (p >= 2)
    {
        if (p >= 8)
        {
            cout << "Province or ";
        }
        else if (p >= 5)
        {
            cout << "Duchy or ";
        }
        else
        {
            cout << "Estate or ";
        }
    }
    if (p >= 6)
    {
        cout << "Gold" << endl;
    }
    else if (p >= 3)
    {
        cout << "Silver" << endl;
    }
    else
    {
        cout << "Copper" << endl;
    }
}
