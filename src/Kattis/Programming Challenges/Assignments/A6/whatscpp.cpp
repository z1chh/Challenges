#include <iostream>
#include <map>

using namespace std;

void test();

int main()
{
    test();
    return 0;
}

void test()
{
    map<int, int> m;
    m[1] = 1;
    m[2] = 1;
    m[5] = 2;
    cout << m[1] << endl;
    cout << m[2] << endl;
    cout << m[5] << endl;
    for (int i = 10; i < 20; i++)
    {
        cout << "Value of " << i << ": " << m[i] << endl;
    }
}