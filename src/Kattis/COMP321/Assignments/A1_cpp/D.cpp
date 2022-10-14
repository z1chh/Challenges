#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    int tc;
    cin >> tc;

    char *str;

    for (int i = 0; i < tc; i++)
    {
        cout << "Case " << i + 1 << endl;
        cin >> str;
        cout << "Displaying array..." << endl;
        for (int i = 0; i < sizeof(str) / sizeof(str[0]); i++)
        {
            cout << str[i] << " ";
        }
        cout << endl
             << "Array displayed..." << endl;
        char alphabet[26] =
            {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        for (int j = 0; j < sizeof(str) / sizeof(str[0]); j++)
        {
            char c = str[j];
            if (c >= 'A' && c <= 'Z')
            {
                c += 32;
            }
            if (c >= 'a' && c <= 'z')
            {
                alphabet[c - 97] = ' ';
            }
        }
        int missing = 0;
        char missing_letters[26];
        for (int j = 0; j < 26; j++)
        {
            if (alphabet[j] == j + 97)
            {
                missing_letters[missing++] = j + 97;
            }
        }
        if (missing == 0)
        {
            cout << "pangram" << endl;
        }
        else
        {
            cout << "missing";
            for (int j = 0; j < missing; j++)
            {
                cout << missing_letters[j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}