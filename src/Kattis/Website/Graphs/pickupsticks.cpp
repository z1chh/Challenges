#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{
    // Get number of vertices and edges
    int vertices, edges, v1, v2;
    cin >> vertices >> edges;

    // Initialize graph
    vector<vector<int>> neighbors(vertices);
    vector<int> deg(vertices + 1, 0);

    // Add edges to graph
    for (int i = 0; i < edges; i++)
    {
        cin >> v1 >> v2;
        neighbors.at(v1 - 1).push_back(v2 - 1);
    }

    // Output graph
    for (auto &v : neighbors)
    {
        for (int i : v)
        {
            cout << i << " ";
        }
        cout << endl;
    }

    // DFS
    vector<int> stack;
    set<int> marked;
    vector<int> order; // This is bs gotta change the logic behind it
    int popped;
    bool isMarked, hasNeighbors;
    stack.push_back(0);
    marked.insert(0);
    while (stack.size() > 0)
    {
        popped = stack.back();
        cout << "Popping from stack: " << popped + 1 << endl;
        stack.pop_back();

        // Push unmarked neighbors
        hasNeighbors = false;
        for (int curNeighbor: neighbors.at(popped))
        {
            // Check if neighbor is marked
            isMarked = false;
            for (int v : marked)
            {
                if (v == curNeighbor)
                {
                    isMarked = true;
                    break;
                }
            }

            if (!isMarked)
            {
                stack.push_back(curNeighbor);
                marked.insert(curNeighbor);
                hasNeighbors = true;
            }
        }

        // Add if no unmarked neighbors
        if (!hasNeighbors)
        {
            order.push_back(popped); // Works if I pop from graph and DFS again
        }
    }

    // Output results
    for (int i = 0; i < order.size(); i++)
    {
        cout << order.at(i) + 1 << endl;
    }

    // Successful return
    return 0;
}                                                                                                                                                                                                                              
