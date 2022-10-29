#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>

using namespace std;

bool DFS(string s, bool *possible, set<string> walter, set<string> jesse, map<string, set<string>> ingredients);

int main()
{
    int items, pairs;
    string item, item1, item2;
    cin >> items;
    map<string, set<string>> ingredients;
    set<string> walter;
    set<string> jesse;
    bool possible = true;
    vector<string> v;

    for (int i = 0; i < items; i++)
    {
        cin >> item;
        ingredients[item] = set<string>();
        v.push_back(item);
    }

    cin >> pairs;
    for (int i = 0; i < pairs; i++)
    {
        cin >> item1 >> item2;
        ingredients[item1].insert(item2);
        ingredients[item2].insert(item1);
    }

    for (string s : v)
    {
        DFS(s, &possible, walter, jesse, ingredients);
    }

    if (possible)
    {
        for (string s : walter)
        {
            cout << s << " ";
        }
        for (string s : jesse)
        {
            cout << s << " ";
        }
    }
    else
    {
        cout << "impossible" << endl;
    }

    return 0;
}

bool DFS(string s, bool *possible, set<string> walter, set<string> jesse, map<string, set<string>> ingredients)
{
    if (walter.find(s) == walter.end() && jesse.find(s) == jesse.end())
    {
        walter.insert(s);
    }
    for (string str : ingredients[s])
    {
        if (walter.find(s) != walter.end() && walter.find(str) == walter.end() && jesse.find(str) == jesse.end())
        {
            jesse.insert(str);
            DFS(str, possible, walter, jesse, ingredients);
        }
        else if (jesse.find(s) != jesse.end() && walter.find(str) == walter.end() && jesse.find(str) == jesse.end())
        {
            walter.insert(str);
            DFS(str, possible, walter, jesse, ingredients);
        }
        else if ((walter.find(s) != walter.end() && walter.find(str) != walter.end()) || (jesse.find(s) != jesse.end() && jesse.find(str) != jesse.end()))
        {
            *possible = false;
        }
    }
    return true;
}
