#include <iostream>
#include <map>
#include <set>

using namespace std;

bool solution(int N, int *A, int *B)
{
    map<int, set<int>> graph;
    for (int i = 0; i < N; i++)
    {
        if (A[i] < B[i])
        {
            graph[A[i]].insert(B[i]);
        }
        else
        {
            graph[B[i]].insert(A[i]);
        }
    }
    for (int i = 1; i < N; i++)
    {
        if (graph[i].size() == 0)
        {
            return false;
        }
        else
        {
            bool found = false;
            for (int n: graph[i])
            {
                if (n == i + 1)
                {
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    int arr1[] = {1};
    int arr2[] = {2};
    cout << solution(2, arr1, arr2) << endl;
    int arr3[] = {2};
    int arr4[] = {1};
    cout << solution(2, arr3, arr4) << endl;
    int arr5[] = {1, 2};
    int arr6[] = {2, 3};
    cout << solution(3, arr5, arr6) << endl;
    int arr7[] = {3, 2};
    int arr8[] = {2, 1};
    cout << solution(3, arr7, arr8) << endl;
    int arr9[] = {1, 2, 3, 4, 5};
    int arr10[] = {2, 3, 4, 5, 6};
    cout << solution(6, arr9, arr10) << endl;
    int arr11[] = {1, 2, 3};
    int arr12[] = {2, 3, 1};
    cout << solution(4, arr11, arr12) << endl;
}