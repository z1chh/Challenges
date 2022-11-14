#include <iostream>

using namespace std;

int main()
{
    int cases, turtles, outsiders, last;
    cin >> cases;
    for (int i = 0; i < cases; i++)
    {
        outsiders = 0;
        cin >> last;
        while (true)
        {
            cin >> turtles;
            if (turtles == 0)
            {
                break;
            }
            if (turtles > 2 * last)
            {
                outsiders += turtles - 2 * last;
            }
            last = turtles;
        }
        cout << outsiders << endl;
    }
    return 0;
}
