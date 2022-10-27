#include <iostream>
#include <string>
#include <cmath>
#include <utility>

using namespace std;

int main()
{
    int height, max_idx = 0, row_nodes, idx = 0;
    pair<int, pair<int, int>> nodes_per_level[height + 1];
    string path;
    cin >> height >> path;

    for (int i = height; i >= 0; i--)
    {
        row_nodes = pow(2, i);
        max_idx += row_nodes;
        nodes_per_level[i] = make_pair(row_nodes, max_idx);
    }
}

// int max_node=2ala height + 1