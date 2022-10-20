#include <iostream>
#include <cstdlib>

using namespace std;

void update(int *a, int *b);

int main()
{
    int a, b;
    int *pA = &a, *pB = &b;
    cin >> a >> b;
    update(pA, pB);
    cout << a << endl
         << b << endl;
    return 0;
}

void update(int *a, int *b)
{
    int tmp = *a;
    *a = *a + *b;
    *b = abs(tmp - *b);
}
