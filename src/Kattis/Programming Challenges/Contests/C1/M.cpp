#include <iostream>

using namespace std;

int main()
{
    int C, n, leave, enter, stay, num_passengers = 0;
    cin >> C >> n;
    bool possible = true;
    for (int i = 0; i < n; i++)
    {
        cin >> leave >> enter >> stay;
        num_passengers -= leave;
        if (num_passengers < 0)
        {
            possible = false;
            break;
        }
        num_passengers += enter;
        if (num_passengers > C)
        {
            possible = false;
            break;
        }
        if (num_passengers < C && stay > 0)
        {
            possible = false;
            break;
        }
    }
    if (num_passengers != 0)
    {
        possible = false;
    }
    if (possible)
    {
        cout << "possible" << endl;
    }
    else
    {
        cout << "impossible" << endl;
    }
    return 0;
}
