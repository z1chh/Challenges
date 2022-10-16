#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Declare vars
    int test_cases;
    string num;

    // Get input
    cin >> test_cases;

    // Compute magnitude
    for (int i = 0; i < test_cases; i++)
    {
        cin >> num;
        cout << num.size() << endl;
    }

    // Successful return
    return 0;
}
