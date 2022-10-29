#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Get input
    string pattern, text;
    int position;
    while (getline(cin, pattern))
    {
        getline(cin, text);

        // Find occurences of pattern
        position = text.find(pattern);
        while (position != string::npos)
        {
            cout << position << " ";
            position = text.find(pattern, position + 1);
        }
        cout << endl;
    }

    // Successful return
    return 0;
}
