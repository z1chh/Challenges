#include <iostream>

using namespace std;

// Remove struct before submitting
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Started LeetCode Problem Merge Two Sorted Lists
class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode to_return = ListNode();
        int val1, val2;
        while (list1->next != nullptr && list2->next != nullptr)
        {
            val1 = list1->val;
            val2 = list2->val;
            if (val1 > val2)
            {
                to_return.next = &ListNode(val2);
            }
        }
    }
};
