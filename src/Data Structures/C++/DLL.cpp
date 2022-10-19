/*
================================================
Name          : DLL.cpp
Author        : Zi Chen Hu
Description   : DLL Structure using Node  object
================================================
 */

#include <iostream>
#include "Node.cpp"

using namespace std;

/**
 * Class DLLStructure
 *
 * @param aFirst Node pointer that points to the first Node of the DLLStructure.
 * @param aLast Node pointer that points to the last Node of the DLLStructure.
 *
 */
class DLLStructure
{
public:
    // Constructors
    DLLStructure() : // Default constructor
                     aFirst(nullptr),
                     aLast(nullptr)
    {
        // cout << "Default constructor for DLLStructure got called." << endl;
    }

    DLLStructure(int array[], int size) // Personalized constructor
    {
        if (size == 0) // Empty array.
        {
            this->aFirst = nullptr;
            this->aLast = nullptr;
        }

        // Initialize the first Node manually.
        Node *firstNode = new Node(array[0], nullptr, nullptr);
        this->aFirst = firstNode;

        // Node pointers to the previous, current and last Nodes.
        Node *curNode;
        Node *previousNode = firstNode;
        Node *last;

        // We first initialize all the Nodes with their pointer to the previous Node.
        for (int i = 1; i < size; i++)
        {
            curNode = new Node(array[i], nullptr, previousNode);
            previousNode = curNode;

            // Update the aLast parameter.
            if (i == (size - 1))
            {
                last = curNode;
                this->aLast = last;
            }
        }

        // We then update the value of the aPrevious parameter for every Node.
        curNode = last;
        previousNode = last->aPrevious;

        for (int i = 1; i < size; i++)
        {
            previousNode->aNext = curNode;
            curNode = previousNode;
            previousNode = curNode->aPrevious;
        }

        // cout << "Personalized constructor for DLLStructure got called." << endl;
    }

    // Destructor
    ~DLLStructure()
    {
        // Make sure that it is not an empty DLLStructure.
        if (this->aFirst != nullptr)
        {
            while (this->aFirst->aNext != nullptr)
            {
                Node *temp = this->aFirst;
                this->aFirst = this->aFirst->aNext;
                delete temp;
            }
            delete this->aFirst;
        }
        // cout << "Destructor for DLLStructure got called." << endl;
    }

    // Methods for other questions:
    void PrintDLL();
    void InsertAfter(int valueToInsertAfter, int valueToBeInserted);
    void InsertBefore(int valueToInsertBefore, int valueToBeInserted);
    void Delete(int value);
    void Sort();
    bool IsEmpty();
    int GetHead();
    int GetTail();
    int GetSize();
    int GetMax();
    int GetMin();
    DLLStructure(DLLStructure &dlls);

private:
    Node *aFirst;
    Node *aLast;
};

/**
 * PrintDLL
 *
 * DLLStructure method to print the value of every Node to the screen.
 */
void DLLStructure::PrintDLL()
{
    // First check that the DLLStructure is not empty.
    if (this->aFirst != nullptr)
    {
        cout << this->aFirst->aData << ", ";

        if (this->aFirst != this->aLast)
        {
            Node *curNode = this->aFirst;
            while (true)
            {
                curNode = curNode->aNext;
                cout << curNode->aData;

                // We break of the while loop if we just "cout"ed the last element.
                if (curNode == this->aLast)
                {
                    break;
                }
                else
                {
                    cout << ", ";
                }
            }
        }
        cout << endl;
    }
}

/**
 * InsertAfter
 *
 * DLLStructure method to insert a Node after the Node with data valueToInsertAfter.
 */
void DLLStructure::InsertAfter(int valueToInsertAfter, int valueToBeInserted)
{
    // First check that the DLLStructure is not empty.
    if (this->aFirst != nullptr)
    {
        Node *newNode;
        bool added = false; // Boolean to check if valueToInsertAfter was found.

        if (this->aFirst->aData == valueToInsertAfter)
        {
            newNode = new Node(valueToBeInserted, this->aFirst->aNext, this->aFirst);
            this->aFirst->aNext->aPrevious = newNode;
            this->aFirst->aNext = newNode;
            added = true;
        }
        else
        {
            Node *tempNode = this->aFirst;
            while (tempNode->aNext != nullptr)
            {
                tempNode = tempNode->aNext;
                if (tempNode->aData == valueToInsertAfter)
                {
                    // We make sure that the Node is not the last one.
                    if (tempNode == this->aLast)
                    {
                        newNode = new Node(valueToBeInserted, nullptr, tempNode);
                        tempNode->aNext = newNode;
                        added = true;
                    }
                    else
                    {
                        newNode = new Node(valueToBeInserted, tempNode->aNext, tempNode);
                        tempNode->aNext->aPrevious = newNode;
                        tempNode->aNext = newNode;
                        added = true;
                    }

                    break;
                }
            }
        }
        // We check if valueToInsertAfter was found:
        if (!added)
        {
            // Otherwise, we add the value at the end of the DLLStructure.
            newNode = new Node(valueToBeInserted, nullptr, this->aLast);
            this->aLast->aNext = newNode;
            this->aLast = newNode;
        }
    }
}

/**
 * InsertBefore
 *
 * DLLStructure method to insert a Node before the Node with data valueToInsertBefore.
 */
void DLLStructure ::InsertBefore(int valueToInsertBefore, int valueToBeInserted)
{
    if (this->aFirst != nullptr)
    {
        if (this->aFirst->aData == valueToInsertBefore)
        {
            Node *newNode = new Node(valueToBeInserted, this->aFirst, nullptr);
            this->aFirst->aPrevious = newNode;
            this->aFirst = newNode;
        }
        // We first want to make sure valueToInsertBefore is a valid value:
        Node *tempNode = this->aFirst;
        bool validValue = false;
        while (tempNode->aNext != nullptr)
        {
            tempNode = tempNode->aNext;
            if (tempNode->aData == valueToInsertBefore)
            {
                validValue = true;
                break;
            }
        }
        // If valueToInsertBefore is a valid value, we use DLLStructure::InsertAfter to insert the new Node.
        if (validValue)
        {
            tempNode = this->aFirst;
            while (tempNode->aNext != nullptr)
            {
                tempNode = tempNode->aNext;
                if (tempNode->aData == valueToInsertBefore)
                {
                    DLLStructure::InsertAfter(tempNode->aPrevious->aData, valueToBeInserted);
                    break;
                }
            }
        }
        // Otherwise, we add the value at the beginning.
        else
        {
            Node *newNode = new Node(valueToBeInserted, this->aFirst, nullptr);
            this->aFirst->aPrevious = newNode;
            this->aFirst = newNode;
        }
    }
}

/**
 * Delete
 *
 * DLLStructure method to delete the Node with data value.
 * Do nothing if there is no Node with such data.
 */
void DLLStructure::Delete(int value)
{
    if (this->aFirst != nullptr)
    {
        Node *tempNode;
        if (this->aFirst->aData == value)
        {
            tempNode = this->aFirst->aNext;
            delete this->aFirst;
            this->aFirst = tempNode;
        }
        else if (this->aLast->aData == value)
        {
            tempNode = this->aLast->aPrevious;
            delete this->aLast;
            this->aLast = tempNode;
        }
        else
        {
            tempNode = this->aFirst;
            while (tempNode->aNext != nullptr)
            {
                tempNode = tempNode->aNext;
                if (tempNode->aData == value)
                {
                    tempNode->aPrevious->aNext = tempNode->aNext;
                    tempNode->aNext->aPrevious = tempNode->aPrevious;
                    delete tempNode;

                    break;
                }
            }
        }
    }
}

/**
 * Sort
 *
 * DLLStructure method to sort the Nodes in ascending order.
 */
void DLLStructure::Sort()
{
    if (this->aFirst != nullptr)
    {
        // We first want to get the size of the DLLStructure.
        int size = 1;
        Node *curNode = this->aFirst;
        while (curNode->aNext != nullptr)
        {
            curNode = curNode->aNext;
            size++;
        }

        // We initialize an array with the parameter aData of each Node.
        int dataArray[size];
        curNode = this->aFirst;
        for (int i = 0; i < size; i++)
        {
            dataArray[i] = curNode->aData;
            curNode = curNode->aNext;
        }

        // SelectionSort:
        int smallest;
        for (int i = 0; i < (size - 1); i++)
        {
            // We first iterate through every element to find the smallest one.
            smallest = i;
            for (int j = (i + 1); j < size; j++)
                if (dataArray[j] < dataArray[smallest])
                    smallest = j;

            // We put the smallest element in front of the other larger values.
            int temp = dataArray[smallest];
            dataArray[smallest] = dataArray[i];
            dataArray[i] = temp;
        }

        // We then update the order of the elements.
        curNode = this->aFirst; // We reset the pointer since it became a null pointer (this->aLast->aNext).
        for (int i = 0; i < size; i++)
        {
            curNode->aData = dataArray[i];
            curNode = curNode->aNext;
        }
    }
}

/**
 * IsEmpty
 *
 * DLLStructure method to check if the DLLStructure is empty.
 * @return true if the DLLStructure is empty.
 * @return false if the DLLStructure is not empty.
 */
bool DLLStructure::IsEmpty()
{
    if (this->aFirst == nullptr)
    {
        return true;
    }
    else
    {
        return false;
    }
}

/**
 * GetHead
 *
 * DLLStructure method to return the first Node of the DLLStructure.
 * @pre this->aFirst != nullptr;
 * @return pData the aData parameter of the first Node of the DLLStructure.
 */
int DLLStructure::GetHead()
{
    // Note that we assume that this->aFirst is not a nullptr (we could check for it and crash the program otherwise, but we decide to simply assume it).
    int pData = this->aFirst->aData;
    return pData;
}

/**
 * GetTail
 *
 * DLLStructure method to return the last Node of the DLLStructure.
 * @pre this->aLast != nullptr;
 * @return pData the aData parameter of the last Node of the DLLStructure.
 */
int DLLStructure::GetTail()
{
    // Note that we assume that this->aLast is not a nullptr (we could check for it and crash the program otherwise, but we decide to simply assume it).
    int pData = this->aLast->aData;
    return pData;
}

/**
 * GetSize
 *
 * DLLStructure method to return the number of Nodes in the DLLStructure.
 * @return size the number of Nodes in the DLLStructure.
 */
int DLLStructure::GetSize()
{
    if (this->aFirst == nullptr)
    {
        return 0;
    }

    int size = 1;
    Node *curNode = this->aFirst;
    while (curNode->aNext != nullptr)
    {
        curNode = curNode->aNext;
        size++;
    }
    return size;
}

/**
 * GetMax
 *
 * DLLStructure method to return the highest value stored in the Nodes.
 * @pre this.GetSize != 0;
 * @return max the parameter aData of the Node that has the highest value of aData.
 */
int DLLStructure::GetMax()
{
    // Note that we assume that this.GetSize != 0 (we could check for it and crash the program otherwise, but we decide to simply assume it).
    int max = this->aFirst->aData;
    Node *curNode = this->aFirst;
    while (curNode->aNext != nullptr)
    {
        curNode = curNode->aNext;
        if (curNode->aData > max)
        {
            max = curNode->aData;
        }
    }
    return max;
}

/**
 * GetMin
 *
 * DLLStructure method to return the lowest value stored in the Nodes.
 * @pre this.GetSize != 0;
 * @return min the parameter aData of the Node that has the lowest value of aData.
 */
int DLLStructure::GetMin()
{
    // Note that we assume that this.GetSize != 0 (we could check for it and crash the program otherwise, but we decide to simply assume it).
    int min = this->aFirst->aData;
    Node *curNode = this->aFirst;
    while (curNode->aNext != nullptr)
    {
        curNode = curNode->aNext;
        if (curNode->aData < min)
        {
            min = curNode->aData;
        }
    }
    return min;
}

/**
 * DLLStructure
 *
 * DLLStructure constructor that performs a deep copy of the given DLLStructure.
 * @pre dlls != null;
 * @param dlls the DLLStructure on which we perform a deep copy.
 * @return newDLL the address of the new DLLStructure.
 */
DLLStructure::DLLStructure(DLLStructure &dlls)
{
    // Note that we assume dlls is a DLLStructure with at least one Node.
    int size = 1;
    Node *curNode = dlls.aFirst;
    while (curNode->aNext != nullptr)
    {
        curNode = curNode->aNext;
        size++;
    }
    int dataArray[size];

    curNode = dlls.aFirst;
    for (int i = 0; i < size; i++)
    {
        dataArray[i] = curNode->aData;
        curNode = curNode->aNext;
    }

    // Initialize the first Node manually.
    Node *firstNode = new Node(dataArray[0], nullptr, nullptr);
    this->aFirst = firstNode;

    // Node pointers to the previous, current and last Nodes.
    Node *previousNode = firstNode;
    Node *last;

    // We first initialize all the Nodes with their pointer to the previous Node.
    for (int i = 1; i < size; i++)
    {
        curNode = new Node(dataArray[i], nullptr, previousNode);
        previousNode = curNode;

        // Update the aLast parameter.
        if (i == (size - 1))
        {
            last = curNode;
            this->aLast = last;
        }
    }

    // We then update the value of the aPrevious parameter for every Node.
    curNode = last;
    previousNode = last->aPrevious;

    for (int i = 1; i < size; i++)
    {
        previousNode->aNext = curNode;
        curNode = previousNode;
        previousNode = curNode->aPrevious;
    }
    cout << "Personalized copy constructor for DLLStructure got called." << endl;
}

// Main function
int main()
{
    cout << "Program started..." << endl
         << endl;

    // Constructor and PrintDLL():
    cout << "Creating DLL with [11, 2, 7, 22, 4]:" << endl;
    int array[5] = {11, 2, 7, 22, 4};
    DLLStructure dll(array, 5);
    dll.PrintDLL(); // The output should be: 11, 2, 7, 22, 4

    // InsertAfter()
    cout << endl
         << endl
         << "Inserting 13 after 7:" << endl;
    dll.InsertAfter(7, 13); // To insert 13 after the first occurence of 7
    dll.PrintDLL();         // the output should be: 11, 2, 7, 13, 22, 4
    cout << "Inserting 25 after 7:" << endl;
    dll.InsertAfter(25, 7); // To insert 7 after the first occurence of 25
    dll.PrintDLL();         // the output should be: 11, 2, 7, 13, 22, 4, 7

    // InsertBefore()
    cout << endl
         << endl
         << "Inserting 26 before 7:" << endl;
    dll.InsertBefore(7, 26); // To insert 26 before the first occurence of 7
    dll.PrintDLL();          // the output should be: 11, 2, 26, 7, 13, 22, 4, 7
    cout << "Inserting 12 after 19:" << endl;
    dll.InsertBefore(19, 12); // To insert 12 before the first occurence of 19
    dll.PrintDLL();           // the output should be: 12, 11, 2, 26, 7, 13, 22, 4, 7

    // Delete()
    cout << endl
         << endl
         << "Deleting 22:" << endl;
    dll.Delete(22);
    dll.PrintDLL(); // the output should be: 12, 11, 2, 26, 7, 13, 4, 7

    // Sort()
    cout << endl
         << endl
         << "Sorting DLL:" << endl;
    dll.Sort();
    dll.PrintDLL(); // the output should be: 2, 4, 7, 7, 11, 12, 13, 26

    // IsEmpty()
    cout << endl
         << endl
         << "Checking if DLL is empty:" << endl;
    if (dll.IsEmpty())
    {
        cout << "The list is empty." << endl;
    }
    else
    {
        cout << "The list is not empty." << endl;
    }

    // GetHead() and GetTail()
    cout << endl
         << endl
         << "Head and Tail elements:" << endl;
    cout << "Head element is: " << dll.GetHead() << endl;
    cout << "Tail element is: " << dll.GetTail() << endl;

    // GetSize()
    cout << endl
         << endl
         << "Getting the size of the DLL:" << endl;
    cout << "Number of elements in the list is: " << dll.GetSize() << endl;

    // GetMax() and GetMin()
    cout << endl
         << endl
         << "Max and Min elements:" << endl;
    cout << "Max element is: " << dll.GetMax() << endl;
    cout << "Min element is: " << dll.GetMin() << endl;

    // Done!
    cout << endl
         << "Main function done!" << endl
         << endl;
    return 0;
}
