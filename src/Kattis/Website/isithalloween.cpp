#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    int d;
    cin >> s >> d;
    if ((s == "OCT" && d == 31) || (s == "DEC" && d == 25))
    {
        cout << "yup" << endl;
    }
    else
    {
        cout << "nope" << endl;
    }
}
