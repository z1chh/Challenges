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
        ListNode *to_return = new ListNode();
        ListNode *copy = to_return;
        int val1, val2;
        while (list1 != nullptr && list2 != nullptr)
        {
            val1 = list1->val;
            val2 = list2->val;
            if (val1 > val2)
            {
                copy->next = new ListNode(val2);
                list2 = list2->next;
                copy = copy->next;
            }
            else
            {
                copy->next = new ListNode(val1);
                list1 = list1->next;
                copy = copy->next;
            }
        }
        if (list1 != nullptr)
        {
            copy->next = list1;
        }
        else if (list2 != nullptr)
        {
            copy->next = list2;
        }
        return to_return->next;
    }
};
