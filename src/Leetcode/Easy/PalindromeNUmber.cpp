#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    bool isPalindrome(int x)
    {
        // Check if x is negative
        if (x < 0)
        {
            return false;
        }

        // Convert x to string
        string s = to_string(x);
        for (int i = 0; i < s.length() / 2; i++)
        {
            if (s[i] != s[s.length() - 1 - i])
            {
                return false;
            }
        }
        return true;
    }
};
