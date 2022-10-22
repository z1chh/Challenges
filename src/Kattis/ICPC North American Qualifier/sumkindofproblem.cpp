#include <iostream>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++)
    {
        int testnum;
        cin >> testnum;
        int N;
        cin >> N;
        cout << testnum << " " << N * (N + 1) / 2 << " " << N * N << " " << N * (N + 1) << endl;
    }
    return 0;
}
