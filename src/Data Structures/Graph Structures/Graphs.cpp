#include <iostream>

using namespace std;

class MatrixGraph
{
public:
    // Attributes
    int numNodes;
    int **matrix;

    // Constructor
    MatrixGraph(int totalNodes);

    // Destructor
    ~MatrixGraph();

    // Other methods
    bool addEdge(int node1, int node2);
};

MatrixGraph::MatrixGraph(int totalNodes)
{
    this->numNodes = totalNodes;
    this->matrix = new int[totalNodes][totalNodes];
    for (int i = 0; i < this->numNodes; i++)
    {
        this->matrix[i] = new int[totalNodes];
    }
}

MatrixGraph::~MatrixGraph()
{
    for (int i = 0; i < this->numNodes; i++)
    {
        delete[] this->matrix[i];
    }
    delete[] this->matrix;
}

bool MatrixGraph::addEdge(int node1, int node2)
{
    if (this->matrix[node1][node2] != 0)
    {
        return false;
    }
    else
    {
        this->matrix[node1][node2] = 1;
        return true;
    }
}

int main()
{
    MatrixGraph m = MatrixGraph(5);
}