#include <iostream>

using namespace std;

void print_arr(int *arr, int size);
bool add_input_house(int *input_houses, int *cur_size, int house);
int get_unused_houses(int *input_houses, int *unused_houses, int total_houses);
bool contains(int *input_houses, int num_houses, int house);
void t1();

int main()
{
    t1();
}

void t1()
{
    int arr[] = {1, 2, 4, 6};
    int size = 5;
    bool added = add_input_house(arr, &size, 4);
    cout << size << " " << added << endl;
    print_arr(arr, size);
    added = add_input_house(arr, &size, 5);
    cout << size << " " << added << endl;
    print_arr(arr, size);

    int un[8];
    for (int i = 0; i < 8; i++)
    {
        un[i] = 0;
    }
    get_unused_houses(arr, un, 8);
    print_arr(un, 8);
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

bool add_input_house(int *input_houses, int *cur_size, int house)
{
    // Check if house already added
    bool already_added = contains(input_houses, *cur_size, house);

    // Add if not added
    if (!already_added)
    {
        input_houses[(*cur_size)++] = house;
    }

    // Return whether the house was added or not
    return !already_added;
}

int get_unused_houses(int *input_houses, int *unused_houses, int total_houses)
{
    int counter = 0;
    for (int i = 2; i <= total_houses; i++)
    {
        if (!contains(input_houses, total_houses, i))
        {
            unused_houses[counter++] = i;
        }
    }
    return counter;
}

void print_arr(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}