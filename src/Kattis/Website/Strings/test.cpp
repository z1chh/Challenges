#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{

    string s1 = "hello";
    string s2 = s1.substr(0, 1);
    cout << s1 << " " << s2 << endl;
    vector<int> v = {1, 2, 3};
    v.pop_back();
    return 0;
}
