#include <iostream>
#include <set>

using namespace std;

class Node
{
public:
    Node(int ID):
    movie_ID(ID)
    {
        // cout << "Node Constructor called" << endl;
    }
    
   ~Node()
    {
        // cout << "Node Destructor called" << endl;
    }

    int get_ID()
    {
        return this->movie_ID;
    }

    void add(Node &to_connect)
    {
        this->neighbors.insert(to_connect);
        to_connect.neighbors.insert(*this);
    }

private:
    int movie_ID;
    set<Node> neighbors;
};

class Edge
{
public:
    Edge(Node n1, Node n2):
    node1(n1),
    node2(n2)
    {
        // cout << "Edge Constructor called" << endl;
    }
    
   ~Edge()
    {
        // cout << "Edge Destructor called" << endl;
    }

    Node getFirst()
    {
        return this->node1;
    }

    Node getSecond()
    {
        return this->node2;
    }

private:
    Node node1;
    Node node2;
};

class Graph
{
public:
    Graph()
    {
        // cout << "Graph Constructor called" << endl;
    }
    
   ~Graph()
    {
        // cout << "Graph Destructor called" << endl;
    }

    void add_node(Node node)
    {
        this->nodes.insert(node);
    }

    bool add_edge(Node n1, Node n2)
    {
        if (this->nodes.find(n1) != this->nodes.end() && this->nodes.find(n2) == this->nodes.end())
        {
            this->edges.insert(Edge(n1, n2));
            return true;
        }
        return false;
    }

private:
    set<Node> nodes;
    set<Edge> edges;
};