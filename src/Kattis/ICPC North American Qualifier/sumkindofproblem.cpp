#include <iostream>

using namespace std;

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int i = 0; i < tc; i++)
    {
        int testnum;
        scanf("%d", &testnum);
        int N;
        scanf("%d", &N);
        int s1 = 0, s2 = 0, s3 = 0;
        for (int i = 1; i <= N; i++)
        {
            s1 += i;
            s2 += (i - 1) * 2 + 1;
            s3 += i * 2;
        }
        printf("%d %d %d %d\n", testnum, s1, s2, s3);
    }
    return 0;
}
