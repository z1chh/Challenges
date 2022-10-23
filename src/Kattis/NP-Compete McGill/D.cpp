#include <iostream>

using namespace std;

int main()
{
    int n, k, num, ct = 0;
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        if (++ct == k)
        {
            cout << num << " ";
            ct = 0;
        }
    }
    cout << endl;
    return 0;
}
