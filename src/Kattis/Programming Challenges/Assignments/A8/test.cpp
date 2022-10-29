#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s = "0123456789";
    string s2 = s.substr(1, 3);
    cout << s2 << endl;

    for (int i = 0; i < 10; i++)
    {
        cout << s.substr(i, i) << endl;
    }
    return 0;
}