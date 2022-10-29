#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int items, pairs;
    string s;
    cin >> items;
    map<string, set<string>> ingredients;
    set<string> a;
    set<string> b;
    bool possible = true;
    vector<string> v;

    for (int i = 0; i < items; i++)
    {
        cin >> s;
        ingredients[s] = set<string>();
        v.push_back(s);
    }
}