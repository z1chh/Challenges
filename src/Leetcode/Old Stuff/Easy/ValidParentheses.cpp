#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        vector<char> brackets;
        for (char c : s)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                brackets.push_back(c);
            }
            else
            {
                if (brackets.empty())
                {
                    return false;
                }
                else
                {
                    if (c == ')')
                    {
                        if (brackets.back() != '(')
                        {
                            return false;
                        }
                        brackets.pop_back();
                    }
                    else if (c == ']')
                    {
                        if (brackets.back() != '[')
                        {
                            return false;
                        }
                        brackets.pop_back();
                    }
                    else if (c == '}')
                    {
                        if (brackets.back() != '{')
                        {
                            return false;
                        }
                        brackets.pop_back();
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
        if (brackets.empty())
        {
            return true;
        }
        return false;
    }
};
