#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

// Function Declarations
bool add_input_house(int *input_houses, int *cur_size, int house);
bool contains(int *input_houses, int num_houses, int house);
int get_unused_houses(int *input_houses, int *unused_houses, int num_houses);

// Union-Find class
class UnionFind
{
public:
    map<int, int> repr;
    int size;

    UnionFind()
    {
        this->repr[1] = 1;
        this->size = 1;
    }

    int find(int value)
    {
        if (this->repr[value] == value)
        {
            return value;
        }
        else
        {
            return this->find(this->repr[value]);
        }
    }

    void v_union(int v1, int v2)
    {
        int f1 = this->find(v1), f2 = this->find(v2);
        if (f1 != f2)
        {
            if (f1 == 1)
            {
                this->repr[f2] = f1;
            }
            else
            {
                this->repr[f1] = f2;
            }
        }
    }

    void add(int v1, int v2)
    {
        if (this->repr[v1] != 0)
        {
            if (this->repr[v2] != 0)
            {
                if (this->find(v1) != this->find(v2))
                {
                    this->v_union(v1, v2);
                }
            }
            else
            {
                this->repr[v2] = v1;
                this->size++;
            }
        }
        else
        {
            if (this->repr[v2] != 0)
            {
                this->repr[v1] = v2;
                this->size++;
            }
            else
            {
                this->repr[v1] = v1;
                this->repr[v2] = v1;
                this->size += 2;
            }
        }
    }
};

int main()
{
    // Get input
    int total_houses, connections, first_house, second_house, num_houses = 1, num_unused;
    bool added;
    cin >> total_houses;
    cin >> connections;

    // Initialize vars
    int input_houses[total_houses];
    for (int i = 0; i < total_houses; i++)
    {
        input_houses[i] = 0;
    }
    input_houses[0] = 1;
    UnionFind uf;

    // For each connected houses pair
    for (int i = 0; i < connections; i++)
    {
        // Get input
        cin >> first_house;
        cin >> second_house;

        // Update input houses (first house)
        added = add_input_house(input_houses, &num_houses, first_house);

        // Update input houses (second house)
        added = add_input_house(input_houses, &num_houses, second_house);

        // Add to Union-Find
        if (second_house == 1)
        {
            uf.add(second_house, first_house);
        }
        else
        {
            uf.add(first_house, second_house);
        }
    }

    // Add houses that weren't used as input
    int unconnected_houses[total_houses];
    for (int i = 0; i < total_houses; i++)
    {
        unconnected_houses[i] = 0;
    }
    num_unused = get_unused_houses(input_houses, unconnected_houses, total_houses);

    // Check houses that are not connected
    for (int i = 2; i < num_houses; i++)
    {
        if (uf.find(input_houses[i]) != 1)
        {
            if (!contains(unconnected_houses, num_unused, input_houses[i]))
            {
                unconnected_houses[num_unused++] = input_houses[i];
            }
        }
    }

    // Output results
    sort(unconnected_houses, unconnected_houses + num_unused);
    for (int i = 0; i < num_unused; i++)
    {
        cout << unconnected_houses[i] << endl;
    }

    // Successful exit
    return 0;
}

bool add_input_house(int *input_houses, int *cur_size, int house)
{
    // Check if house already added
    bool exists = false;
    for (int i = 0; i < *cur_size; i++)
    {
        if (input_houses[i] == house)
        {
            exists = true;
            break;
        }
    }

    // Add if not added
    if (!exists)
    {
        input_houses[++*cur_size] = house;
    }

    // Return whether the house was added or not
    return !exists;
}

bool contains(int *input_houses, int num_houses, int house)
{
    for (int i = 0; i < num_houses; i++)
    {
        if (input_houses[i] == house)
        {
            return true;
        }
    }
    return false;
}

int get_unused_houses(int *input_houses, int *unused_houses, int num_houses)
{
    int counter = 0;
    for (int i = 1; i <= num_houses; i++)
    {
        if (!contains(input_houses, num_houses, i))
        {
            unused_houses[counter++] = i;
        }
    }
    return counter;
}