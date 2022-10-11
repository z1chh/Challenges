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
        repr[1] = 1;
    }

    int find(int value)
    {
        if (repr[value] == value)
        {
            return value;
        }
        else
        {
            return find(repr[value]);
        }
    }

    void v_union(int v1, int v2)
    {
        int f1 = find(v1), f2 = find(v2);
        if (f1 != f2)
        {
            if (f1 == 1)
            {
                repr[f2] = f1;
            }
            else
            {
                repr[f1] = f2;
            }
        }
    }

    void add(int v1, int v2)
    {
        if (repr[v1] != 0)
        {
            if (repr[v2] != 0)
            {
                if (find(v1) != find(v2))
                {
                    v_union(v1, v2);
                }
            }
            else
            {
                repr[v2] = v1;
                size++;
            }
        }
        else
        {
            if (repr[v2] != 0)
            {
                repr[v1] = v2;
                size++;
            }
            else
            {
                repr[v1] = v1;
                repr[v2] = v1;
                size += 2;
            }
        }
    };

    int main()
    {
        // Get input
        int total_houses, connections, first_house, second_house, num_houses = 0;
        bool added;
        cin >> total_houses;
        cin >> connections;

        // Initialize vars
        int input_houses[total_houses];
        UnionFind uf;

        // For each connected houses pair
        for (int i = 0; i < connections; i++)
        {
            // Get input
            cin >> first_house;
            cin >> second_house;

            // Update input houses (first house)
            added = add_input_house(input_houses, num_houses, first_house);
            if (added)
            {
                num_houses += 1;
            }

            // Update input houses (second house)
            added = add_input_house(input_houses, num_houses, second_house);
            if (added)
            {
                num_houses += 1;
            }

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

    bool add_input_house(int *input_houses, int cur_size, int house)
    {
        // Check if house already added
        bool exists = false;
        for (int i = 0; i < cur_size; i++)
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
            input_houses[cur_size + 1] = house;
        }

        // Return whether the house was added or not
        return !exists;
    }

    bool was_added(int *input_houses, int house)
    {
        // TO-DO
        // MY BRAIN DEAD I CANT EVEN THINK
    }