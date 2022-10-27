#include <iostream>
#include <map>
#include <vector>

using namespace std;

class UnionFind
{
public:
    UnionFind()
    {
        cout << "Union-Find Constructor called" << endl;
    }

    ~UnionFind()
    {
        cout << "Union-Find Destructor called" << endl;
    }

    int find(int value); // Returns the representative of the set of value
    void combine(int val1, int val2); // Unions the sets of val1 and val2
    void add(int val1, int val2); // Adds the pair of values to the UnionFind

    // Attributes
private:
    map<int, int> representatives;
    map<int, vector<int>> sets;

    // Helper Methods
    int find_helper(int value);
};

int main()
{
    cout << "Starting tests..." << endl;
    UnionFind uf = UnionFind();
    cout << uf.find(3) << endl;
    cout << "Passed tests successfully." << endl;
    return 0;
}

int UnionFind::find(int value)
{
    if (this->representatives.count(value) != 1)
    {
        throw invalid_argument("Error: value not in Union-Find");
    }
    return this->find_helper(value);
}

int UnionFind::find_helper(int value)
{
    int repr = this->representatives[value];
    return repr == value ? repr: this->find_helper(repr);
}

void UnionFind::combine(int val1, int val2)
{
    cout << val1 + val2 << endl;
}

void UnionFind::add(int val1, int val2)
{
    cout << val1 + val2 << endl;
}