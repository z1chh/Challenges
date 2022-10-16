#include <iostream>
#include <map>

using namespace std;

// Function Declarations
bool add_input_house(int *input_houses, int cur_size, int house);
bool was_added(int *input_houses, int house);

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
                if (v2 == 1)
                {
                    this->repr[v1] = v2;
                    this->repr[v2] = v2;
                }
                else
                {
                    this->repr[v1] = v1;
                    this->repr[v2] = v1;
                }
                this->size += 2;
            }
        }
    }
};

int main()
{
    // Get input
    int total_houses, connections, first_house, second_house, num_houses = 1;
    bool added;
    cin >> total_houses;
    cin >> connections;

    // Initialize vars
    int input_houses[total_houses];
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

bool was_added(int *input_houses, int house)
{
    // TO-DO
    // MY BRAIN DEAD I CANT EVEN THINK
    return false;
}