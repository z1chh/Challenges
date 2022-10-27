#include <iostream>
#include <map>
#include <vector>

using namespace std;

class UnionFind
{
public:
    UnionFind()
    {
        // Nothing
    }

    ~UnionFind()
    {
        // Nothing
    }

    int find(int value); // Returns the representative of the set of value
    void combine(int val1, int val2); // Unions the sets of val1 and val2
    void add(int val1, int val2); // Adds the pair of values to the UnionFind

    // Attributes
    map<int, int> representatives;
private:
    map<int, vector<int>> sets;

    // Helper Methods
    int find_helper(int value);
};

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

int main()
{
    UnionFind uf = UnionFind();
    uf.representatives[1] = 1;
    uf.representatives[2] = 1;
    uf.representatives[3] = 2;
    cout << uf.find(3) << endl;
    return 0;
}