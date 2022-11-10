#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Get number of cases
    int cases;
    cin >> cases;

    int rep, size, idx;
    string inp, pattern, substr;

    // Flush buffer
    getline(cin, pattern);

    for (int x = 0; x < cases; x++)
    {
        // Get input
        getline(cin, inp);
        size = inp.size();

        // Reset vars
        rep = -1;

        for (int i = 1; i < size; i++)
        {
            pattern = inp.substr(0, i);
            idx = i;
            while (idx < size)
            {
                if (idx + i > size)
                {
                    substr = inp.substr(idx, size - idx);
                    pattern = pattern.substr(0, size - idx);
                    idx = size;
                }
                else
                {
                    substr = inp.substr(idx, i);
                    idx += i;
                }
                //cout << "index " << idx << " with pattern \"" << pattern << "\" and substr \"" << substr  << "\"." << endl;
                if (pattern != substr)
                {
                    //cout << "Breaking" << endl;
                    break;
                }
            }

            if (pattern == substr)
            {
                rep = i;
                break;
            }
        }

        // Output answer
        if (rep == -1)
        {
            cout << size << endl;
        }
        else
        {
            cout << rep << endl;
        }
    }

    // Successful return
    return 0;
}
