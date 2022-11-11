#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{
    // Initialize graph
    int vertices, edges, v1, v2;
    cin >> vertices >> edges;
    int graph[vertices][vertices];
    for (int i = 0; i < vertices; i++)
    {
        for (int j = 0; j < vertices; j++)
        {
            graph[i][j] = 0;
        }
    }
    for (int i = 0; i < edges; i++)
    {
        cin >> v1 >> v2;
        graph[v1 - 1][v2 - 1] = 1;
    }

    // Output graph
    for (int i = 0; i < vertices; i++)
    {
        for (int j = 0; j < vertices; j++)
        {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }

    // DFS
    vector<int> stack;
    set<int> marked;
    vector<int> order;
    int popped;
    bool isMarked, hasNeighbors;
    stack.push_back(0);
    marked.insert(0);
    while (stack.size() > 0)
    {
        // Pop the stack
        popped = stack.back();
        cout << "Popping from stack: " << popped + 1 << endl;
        stack.pop_back();

        // Push unmarked neighbors
        hasNeighbors = false;
        for (int i = 0; i < vertices; i++)
        {
            if (graph[popped][i] != 0)
            {
                // Check if neighbor is marked
                isMarked = false;
                for (int v : marked)
                {
                    if (v == i)
                    {
                        isMarked = true;
                        break;
                    }
                }

                if (!isMarked)
                {
                    stack.push_back(i);
                    marked.insert(i);
                    hasNeighbors = true;
                }
            }
        }

        // Add if no unmarked neighbors
        if (!hasNeighbors)
        {
            order.push_back(popped);
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
