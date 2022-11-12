#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    // Get input
    int width, partitions, i, j;
    cin >> width >> partitions;
    int locations[partitions + 2];
    for (i = 0; i < partitions; i++)
    {
        cin >> locations[i];
    }

    // Add start and end to locations
    locations[partitions] = 0;
    locations[partitions + 1] = width;

    // Get all unique location sizes
    set<int> spaces;
    for (i = 0; i < partitions + 1; i++)
    {
        for (j = i + 1; j < partitions + 2; j++)
        {
            spaces.insert(abs(locations[i] - locations[j]));
        }
    }

    // Output results
    for (int space: spaces)
    {
        cout << space << " ";
    }
    cout << endl;

    // Successful return
    return 0;
}
