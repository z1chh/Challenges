#include <iostream>
#include <string>

using namespace std;

int main()
{
    int a, idx = -1, n1, n2;
    string s;
    bool b;
    cin >> a;
    for (int i = 0; i < a; i++)
    {
        b = false;
        cin >> s;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '+')
            {
                b = true;
                idx = i;
                break;
            }
            else if (s[i] == '=')
            {
                break;
            }
        }
        if (b)
        {
            n1 = stoi(s.substr(0, idx));
            n2 = stoi(s.substr(idx + 1, s.size()));
            cout << n1 + n2 << endl;
        }
        else
        {
            cout << "skipped" << endl;
        }
    }
    return 0;
}
