#include <iostream>
#include <cmath>

using namespace std;
// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int X, int Y, int D) {
    // write your code in C++14 (g++ 6.2.0)
    return ceil(((Y - X) / float(D)));
}

int main()
{
    cout << solution(1, 1000000000, 1) << endl;
}
