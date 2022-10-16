#include <iostream>

using namespace std;

int main()
{
    int a, b, d;
    cin >> a >> b;
    if (a < b)
    {
        d = b - a;
        if (d > 1)
        {
            cout << "Dr. Chaz will have " << d << " pieces of chicken left over!" << endl;
        }
        else
        {
            cout << "Dr. Chaz will have 1 piece of chicken left over!" << endl;
        }
    }
    else
    {
        d = a - b;
        if (d > 1)
        {
            cout << "Dr. Chaz needs " << d << " more pieces of chicken!" << endl;
        }
        else
        {
            cout << "Dr. Chaz needs 1 more piece of chicken!" << endl;
        }
    }
    return 0;
}
