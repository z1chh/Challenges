#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    // Declare variables
    int nb;
    string name;
    while (true)
    {
        // Get input
        cin >> nb;
        if (nb == 0)
            break;

        // Store names with their 2 first characters
        string names[nb];
        pair<string, int> names_shortened[nb];
        for (int i = 0; i < nb; i++)
        {
            cin >> name;
            names[i] = name;
            names_shortened[i] = make_pair(name.substr(0, 2), i);
        }

        // Sort names by first two characters
        stable_sort(names_shortened, names_shortened + sizeof(names_shortened) / sizeof(names_shortened[0]));

        // Output names
        for (auto n : names_shortened)
        {
            cout << names[n.second] << endl;
        }
        cout << endl;
    }

    // Successful return
    return 0;
}
