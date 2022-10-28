#include <iostream>
#include <vector>

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

    void add(Node &to_connect)
    {
        this->neighbors.push_back(to_connect);
        to_connect.neighbors.push_back(*this);
    }

private:
    int movie_ID;
    vector<Node> neighbors;
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
private:
    vector<Node> nodes;
    vector<Edge> edges;
};