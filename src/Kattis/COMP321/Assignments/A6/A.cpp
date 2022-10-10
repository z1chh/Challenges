#include <iostream>
#include <map>

using namespace std;

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
        bool exists = 0;
        for (int i = 0; i < size; i++)
        {
            if (repr[i] == value)
            {
                exists = 1;
                break;
            }
        }
    }
};

// Function Declarations
bool add_input_house(int *input_houses, int cur_size, int house);

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
    }
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