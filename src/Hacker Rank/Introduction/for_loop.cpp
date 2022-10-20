#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    map<int, string> eng_repr;
    eng_repr[1] = "one";
    eng_repr[2] = "two";
    eng_repr[3] = "three";
    eng_repr[4] = "four";
    eng_repr[5] = "five";
    eng_repr[6] = "six";
    eng_repr[7] = "seven";
    eng_repr[8] = "eight";
    eng_repr[9] = "nine";

    int a, b;
    cin >> a >> b;
    for (int i = a; i <= b; i++)
    {
        if (i < 10)
        {
            cout << eng_repr[i] << endl;
        }
        else if (i & 1)
        {
            cout << "odd" << endl;
        }
        else
        {
            cout << "even" << endl;
        }
    }
    return 0;
}
