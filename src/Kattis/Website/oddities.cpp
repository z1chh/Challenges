#include <iostream>

using namespace std;

int main()
{
    int a, b;
    cin >> a;
    for (int i = 0; i < a; i++)
    {
        cin >> b;
        if (b & 1) {
            cout << b << " is odd" << endl;
        } else {
            cout << b << " is even" << endl;
        }
    }
    return 0;
}
