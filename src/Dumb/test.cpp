#include <iostream>
#include <string>
#include <utility>

using namespace std;

int main()
{
    float f1 = 1., f2 = 2., f3 = 3., f4;
    f4 = max(f1, f2);
    f4 = max(f4, f3);
    cout << f4 << endl;
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