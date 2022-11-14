#include <iostream>
#include <vector>

using namespace std;

int depth = 0;

vector<int> isEqual(vector<int> v)
{
    depth++;
    int num = v[0];
    bool same = true;
    for (int i : v)
    {
        if (i != num)
        {
            same = false;
            break;
        }
    }

    if (same)
    {
        v.push_back(num);
        return v;
    }

    else
    {
        vector<int> temp;
        for (int i = 0; i < v.size() - 1; i++)
        {
            temp.push_back(v[i] - v[i + 1]);
        }
        temp = isEqual(temp);
        v.push_back(v[v.size() - 1] - temp[temp.size() - 1]);
        return v;
    }
}

int main()
{
    int n;
    cin >> n;

    vector<int> v;

    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        v.push_back(num);
    }

    vector<int> ans = isEqual(v);

    cout << depth - 1 << " " << ans[ans.size() - 1] << endl;
}
