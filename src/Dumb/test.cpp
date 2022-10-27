#include <iostream>
#include <string>
#include <utility>

using namespace std;

int main()
{
    int x, y;
    double z;
    string s;
    cin >> x >> s >> y >> z;
    pair<pair<int, int>, double> a = make_pair(make_pair(x, y), z);
    cout << a.first.first << " " << a.first.second << " " << a.second << endl;
    cout << s << endl;
    return 0;
}