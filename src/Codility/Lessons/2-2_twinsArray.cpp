#include <iostream>
#include <vector>
#include <set>

using namespace std;

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A)
{
    // write your code in C++14 (g++ 6.2.0)
    set<int> s;
    for (int n: A)
    {
        if (s.find(n) != s.end())
        {
            s.erase(n);
        }
        else
        {
            s.insert(n);
        }
    }

    for (int n: s)
    {
        return n;
    }
}
