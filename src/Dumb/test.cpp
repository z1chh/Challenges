#include <iostream>
#include <string>
#include <utility>

using namespace std;

int main()
{
    int x;
    string s = "HI";
    cin >> x;
    while (cin >> s)
    {
        cout << "had input" << endl;
    }
    cout << s << endl;
    return 0;
}