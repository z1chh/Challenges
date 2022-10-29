#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Node
{
public:
    Node(int ID) : movie_ID(ID)
    {
        // cout << "Node Constructor called" << endl;
    }

    ~Node()
    {
        // cout << "Node Destructor called" << endl;
    }

    void add(Node &to_connect)
    {
        this->neighbors.insert(to_connect);
        to_connect.neighbors.insert(*this);
    }

    // Attributes
    int movie_ID;
    set<Node> neighbors;
};

class Edge
{
public:
    Edge(Node *n1, Node *n2) : node1(n1),
                               node2(n2)
    {
        // cout << "Edge Constructor called" << endl;
    }

    ~Edge()
    {
        // cout << "Edge Destructor called" << endl;
    }

    // Attributes
    Node *node1;
    Node *node2;
};

class Graph
{
public:
    Graph()
    {
        Node *h = new Node(-1);
        this->H = h;
        this->nodes.insert(this->H);
    }

    ~Graph()
    {
        for (Node *n : this->nodes)
        {
            delete n;
        }
        for (Edge *e : this->edges)
        {
            delete e;
        }
    }

    void add_node(int node_ID);
    Node *find_node(int node_ID);
    bool add_edge(int node_ID1, int node_ID2);
    set<int> get_neighbors(int node_ID);
    int BFS(int node_ID1, int node_ID2, int n);

    // Attributes
    set<Node *> nodes;
    set<Edge *> edges;
    Node *H;
};

void Graph::add_node(int node_ID)
{
    Node *node = new Node(node_ID);
    this->nodes.insert(node);
}

Node *Graph::find_node(int node_ID)
{
    for (Node *n : this->nodes)
    {
        if (n->movie_ID == node_ID)
        {
            return n;
        }
    }
    throw invalid_argument("Error: No such node");
}

bool Graph::add_edge(int node_ID1, int node_ID2)
{
    if (this->nodes.find(this->find_node(node_ID1)) != this->nodes.end() && this->nodes.find(this->find_node(node_ID2)) == this->nodes.end())
    {
        Edge *edge = new Edge(this->find_node(node_ID1), this->find_node(node_ID2));
        this->edges.insert(edge);
        return true;
    }
    return false;
}

set<int> Graph::get_neighbors(int node_ID)
{
    set<int> neighbors;
    for (Edge *e : this->edges)
    {
        if (e->node1->movie_ID == node_ID)
        {
            neighbors.insert(e->node2->movie_ID);
        }
        else if (e->node2->movie_ID == node_ID)
        {
            neighbors.insert(e->node1->movie_ID);
        }
    }
    return neighbors;
}

int Graph::BFS(int node_ID1, int node_ID2, int n)
{
    // Mark all the vertices as not visited
    vector<bool> visited;
    visited.resize(n, false);

    // Create a queue for BFS
    list<int> queue;

    // Mark the current node as visited and enqueue it
    visited[s] = true;
    queue.push_back(s);

    while (!queue.empty())
    {
        // Dequeue a vertex from queue and print it
        s = queue.front();
        cout << s << " ";
        queue.pop_front();

        // Get all adjacent vertices of the dequeued
        // vertex s. If a adjacent has not been visited,
        // then mark it visited and enqueue it
        for (auto adjecent : adj[s])
        {
            if (!visited[adjecent])
            {
                visited[adjecent] = true;
                queue.push_back(adjecent);
            }
        }
    }
}

int main()
{
    // Get input
    int n, h, l, u, v;
    cin >> n >> h >> l;

    // Initialize graph
    Graph g;
    for (int i = 0; i < n; i++)
    {
        g.add_node(i);
    }

    // Get horror list
    int horror_list[h];
    for (int i = 0; i < h; i++)
    {
        cin >> horror_list[i];
    }

    // Add edges to graph
    for (int i = 0; i < l; i++)
    {
        cin >> u >> v;
        g.add_edge(u, v);
    }

    // Connect H to horror movies
    for (int i = 0; i < h; i++)
    {
        g.add_edge(-1, horror_list[i]);
    }

    // Compute BFS from H to all movies
    int path_lengths[n];
    for (int i = 0; i < n; i++)
    {
        path_lengths[i] = g.BFS(-1, i, n);
    }

    // Output longest path
    int longest_path = -1;
    int best_movie;
    for (int i = 0; i < n; i++)
    {
        if (path_lengths[i] > longest_path)
        {
            longest_path = path_lengths[i];
            best_movie = i;
        }
    }
    cout << best_movie << endl;

    // Successful return
    return 0;
}
