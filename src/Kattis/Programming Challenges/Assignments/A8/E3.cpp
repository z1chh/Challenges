#include <iostream>
#include <string>

using namespace std;

int main()
{
    string pattern, text;
    int pattern_size, text_size;
    while (getline(cin, pattern))
    {
        getline(cin, text);
        pattern_size = pattern.size();
        text_size = text.size();
        /* cout << pattern_size << " " << text_size << endl;
        cout << "Iterating from i = 0 to " << text_size - pattern_size << endl; */
        for (int i = 0; i < text_size - pattern_size + 1; i++)
        {
            /* cout << "Index " << i << ": " << pattern << " " << text.substr(i, pattern_size) << endl; */
            if (pattern == text.substr(i, pattern_size))
            {
                cout << i << " ";
            }
        }
        cout << endl;
    }

    // Successful return
    return 0;
}
