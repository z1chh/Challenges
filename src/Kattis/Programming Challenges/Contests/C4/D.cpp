#include <iostream>

using namespace std;

int main()
{
    // Get input
    int x, y;
    cin >> x >> y;

    // Output corresponding quadrant
    if (x >= 0 && y >= 0)
    {
        cout << 1 << endl;
    }
    else if (x < 0 && y >= 0)
    {
        cout << 2 << endl;
    }
    else if (x < 0 && y < 0)
    {
        cout << 3 << endl;
    }
    else
    {
        cout << 4 << endl;
    }

    // Successful return
    return 0;
}
