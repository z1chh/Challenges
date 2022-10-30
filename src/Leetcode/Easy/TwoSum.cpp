#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> to_return;
        int size = nums.size(), i, j;
        for (i = 0; i < size - 1; i++)
        {
            for (j = i + 1; j < size; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    to_return.push_back(i);
                    to_return.push_back(j);
                    break;
                }
            }
        }
        return to_return;
    }
};
