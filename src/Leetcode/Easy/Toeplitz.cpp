#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
    bool isToeplitzMatrix(vector<vector<int>> &matrix)
    {
        int rows = matrix.size(), cols = matrix[0].size(), num_diags = rows - cols, val;
        if (num_diags == 0)
        {
            val = matrix[0][0];
            for (int i = 1; i < rows; i++)
            {
                if (matrix[i][i] != val)
                {
                    return false;
                }
            }
            return true;
        }
        else if (num_diags > 0)
        {
            int counter = 0;
            for (int x = 0; x < counter; x++)
            {
                val = matrix[0][0 + x];
                for (int i = 0; i < rows; i++)
                {
                    if (matrix[i][i + x] != val)
                    {
                        return false;
                    }
                }
            }
            return true;
        }
        else
        {
            int counter = 0;
            for (int x = 0; x < counter; x++)
            {
                val = matrix[0 + x][0];
                for (int i = 0; i < rows; i++)
                {
                    if (matrix[i + x][i] != val)
                    {
                        return false;
                    }
                }
            }
            return true;
        }
    }
};

int main()
{
    Solution s = Solution();
    vector<vector<int>> v;
    vector<int> a;
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    a.push_back(4);
    v.push_back(a);
    vector<int> b;
    b.push_back(5);
    b.push_back(2);
    b.push_back(1);
    b.push_back(3);
    v.push_back(b);
    cout << s.isToeplitzMatrix(v) << endl;
}