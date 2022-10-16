#include <iostream>

using namespace std;

int main()
{
    int periods;
    cin >> periods;
    double qaly = 0.0;
    double q, y;
    for (int i = 0; i < periods; i++)
    {
        cin >> q >> y;
        qaly += q * y;
    }
    cout << qaly << endl;
    return 0;
}
