#include <iostream>
#include <vector>

using namespace std;
// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int X, vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int max = 0;
    for (int n: A)
    {
        if (n > max)
        {
            max = n;
        }
    }
    return max;
}
