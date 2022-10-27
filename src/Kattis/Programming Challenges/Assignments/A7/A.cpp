#include <iostream>
#include <string>
#include <cmath>
#include <utility>

using namespace std;

int main()
{
    int height, max_idx = 0, row_nodes, idx = 0, tmp;
    string path = "NULL";
    cin >> height;
    while (cin >> path)
    {
        // Nothing
    }
    row_nodes = pow(2, height);
    if (path == "NULL")
    {
        // Simply output the max value of the tree
        cout << row_nodes * 2 - 1 << endl;

        // Successful return
        return 0;
    }
    pair<int, int> nodes_per_level[height + 1];

    for (int i = height; i >= 0; i--)
    {
        nodes_per_level[i] = make_pair(row_nodes, max_idx + 1);
        max_idx += row_nodes;
        row_nodes = row_nodes >> 1; // not SRL but okay since we're working with positive ints (also powers of 2)
    }

    // Get correct node
    int size = path.size();
    pair<int, int> level = nodes_per_level[size];
    int num_nodes = level.first;
    int index = 0;
    for (char c: path)
    {
        num_nodes = num_nodes >> 1;
        if (c == 'L')
        {
            index += num_nodes; // Increment to point to the left subtree instead
        }
    }
    cout << level.second + index << endl;

    return 0;
}
