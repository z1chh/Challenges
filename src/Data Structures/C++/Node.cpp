/*
=============================================
Name          : Node.cpp
Author        : Zi Chen Hu
Description   : Node object for DLL Structure
=============================================
 */

#include <iostream>

using namespace std;

/**
 * Class Node
 *
 * @param aData int that holds the data of the Node.
 * @param aNext Node pointer that points to the next Node.
 * @param aPrevious Node pointer that points to the previous Node.
 *
 */
class Node
{
public:
    int aData;
    Node *aNext;
    Node *aPrevious;

    // Constructors
    Node();

    Node(int pData, Node *pNext, Node *pPrevious);

    // Destructor
    ~Node();
};

// Default constructor
Node::Node() : aData(0),
               aNext(nullptr),
               aPrevious(nullptr)
{
    // cout << "Default constructor for Node got called." << endl;
}

// Personalized constructor
Node::Node(int pData, Node *pNext, Node *pPrevious) : aData(pData),
                                                      aNext(pNext),
                                                      aPrevious(pPrevious)
{
    // cout << "Personalized constructor for Node got called." << endl;
}

// Destructor
Node::~Node()
{
    // No memory allocated dynamically, nothing to destroy manually.
    // cout << "Destructor for Node got called." << endl;
}
