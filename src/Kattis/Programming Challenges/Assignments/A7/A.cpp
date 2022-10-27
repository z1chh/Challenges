#include <iostream>
#include <string>
#include <cmath>
#include <utility>

using namespace std;

int main()
{
    int height, max_idx = 0, row_nodes, idx = 0, tmp;
    string path;
    cin >> height >> path;
    pair<int, pair<int, int>> nodes_per_level[height + 1];
    row_nodes = pow(2, height);

    for (int i = height; i >= 0; i--)
    {
        tmp = max_idx + 1;
        max_idx += row_nodes;
        nodes_per_level[i] = make_pair(row_nodes, make_pair(tmp, max_idx));
        row_nodes = row_nodes >> 1; // not SRL but okay since we're working with positive ints (also powers of 2)
    }

    for (int i = 0; i <= height; i++)
    {
        cout << i << ": " << nodes_per_level[i].first << " " << nodes_per_level[i].second.first << " " << nodes_per_level[i].second.second << endl;
    }

    return 0;
}

// int max_node=2ala height + 1