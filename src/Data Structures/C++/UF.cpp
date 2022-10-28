#include <iostream>
#include <map>
#include <vector>

using namespace std;

class UnionFind
{
public:
    UnionFind()
    {
        // cout << "Union-Find Constructor called" << endl;
    }

    ~UnionFind()
    {
        // cout << "Union-Find Destructor called" << endl;
    }

    int find(int value);              // Returns the representative of the set of value
    void combine(int val1, int val2); // Unions the sets of val1 and val2
    void add(int val1, int val2);     // Adds the pair of values to the UnionFind
    int size(int value);              // Returns the size of the set of value
    void display();                   // Prints the Union-Find structure

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
    uf.add(1, 2);
    uf.add(2, 3);
    uf.add(3, 4);
    uf.add(4, 1);
    uf.add(5, 6);
    uf.add(7, 8);
    uf.add(5, 8);
    cout << "Find" << endl;
    cout << uf.find(3) << endl;
    cout << uf.find(8) << endl;
    cout << uf.find(7) << endl;
    cout << endl
         << "Size" << endl;
    cout << uf.size(3) << endl;
    cout << uf.size(7) << endl;
    cout << "Passed tests successfully." << endl;
    uf.display();
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
    return repr == value ? repr : this->find_helper(repr);
}

void UnionFind::combine(int val1, int val2)
{
    int repr1 = this->representatives[val1];
    int repr2 = this->representatives[val2];
    this->representatives[val2] = repr1;
    for (int i = 0; i < this->sets[repr2].size(); i++)
    {
        this->sets[repr1].push_back(this->sets[repr2].back());
        this->sets[repr2].pop_back();
    }
}

void UnionFind::add(int val1, int val2)
{
    if (this->representatives.count(val1) == 1)
    {
        int repr1 = this->representatives[val1];
        if (this->representatives.count(val2) == 1)
        {
            int repr2 = this->representatives[val2];
            if (repr1 != repr2)
            {
                this->combine(val1, val2);
            }
        }
        else
        {
            this->representatives[val2] = repr1;
            this->sets[val2].push_back(val1);
        }
    }
    else
    {
        if (this->representatives.count(val2) == 1)
        {
            int repr2 = this->representatives[val2];
            this->representatives[val1] = repr2;
            this->sets[val1].push_back(val2);
        }
        else
        {
            this->representatives[val1] = val1;
            this->representatives[val2] = val1;
            this->sets[val1].push_back(val1);
            this->sets[val1].push_back(val2);
        }
    }
}

int UnionFind::size(int value)
{
    return this->sets[this->representatives[value]].size();
}

void UnionFind::display()
{
    cout << "Representatives" << endl;
    for (int i = 0; i < this->representatives.size(); i++)
    {
        cout << i << ": " << this->representatives[i] << endl;
    }
    cout << "Sets" << endl;
    for (int i = 0; i < this->sets.size(); i++)
    {
        cout << i << ": " << this->sets[i].size() << endl;
    }
}
