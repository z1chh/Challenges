#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

int BFS(vector<int> *adjacent_nodes[], set<int> *unvisited_nodes, queue<pair<int, int>> *q);

int main()
{
    // Get input
    int n, h, l;
    cin >> n >> h >> l;
    vector<int> adjacent_nodes[n];
    for (int i = 0; i < n; i++)
    {
        adjacent_nodes[i] = vector<int>();
    }

    set<int> unvisited_nodes = set<int>();
    for (int i = 0; i < n; i++)
    {
        unvisited_nodes.insert(i);
    }

    queue<pair<int, int>> q = queue<pair<int, int>>();

    int horror_movie_ID;
    for (int i = 0; i < h; i++)
    {
        cin >> horror_movie_ID;
        unvisited_nodes.erase(horror_movie_ID);
        q.push(make_pair(0, horror_movie_ID));
    }

    int u, v;
    for (int i = 0; i < l; i++)
    {
        cin >> u >> v;
        adjacent_nodes[u].push_back(v);
        adjacent_nodes[v].push_back(u);
    }

    int c = -1, i = -1, cost, x;
    while (q.size() > 0)
    {
        // Pop from queue
        cost = q.front().first;
        x = q.front().second;
        q.pop();

        if (cost > c || (cost == c && x < i))
        {
            c = cost;
            i = x;
        }
        for (int u : adjacent_nodes[x])
        {
            if (unvisited_nodes.find(u) != unvisited_nodes.end())
            {
                unvisited_nodes.erase(u);
                q.push(make_pair(cost + 1, u));
            }
        }
    }
    if (unvisited_nodes.size() != 0)
    {
        cout << i << endl;
    }
    else
    {
        int smallest = INT_MAX;
        for (int n : unvisited_nodes)
        {
            smallest = min(smallest, n);
        }
        cout << smallest << endl;
    }

    // Successful return
    return 0;
}
