#include <iostream>
#include <string>

using namespace std;

int main()
{
    int cup = 1;
    char c;
    string moves;
    getline(cin, moves);
    for (int i = 0; i < moves.size(); i++)
    {
        c = moves[i];
        if (c == 'A')
        {
            if (cup == 1)
            {
                cup = 2;
            }
            else if (cup == 2)
            {
                cup = 1;
            }
        }
        else if (c == 'B')
        {
            if (cup == 2)
            {
                cup = 3;
            }
            else if (cup == 3)
            {
                cup = 2;
            }
        }
        else
        {
            if (cup == 1)
            {
                cup = 3;
            }
            else if (cup == 3)
            {
                cup = 1;
            }
        }
    }
    cout << cup << endl;
    return 0;
}
