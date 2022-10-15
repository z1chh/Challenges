#include <iostream>
#include <string>

using namespace std;

int main()
{
    int test_cases;
    string num;
    cin >> test_cases;
    for (int i = 0; i < test_cases; i++)
    {
        cin >> num;
        cout << num.size() << endl;
    }
}
