#include <iostream>
#include <string>

using namespace std;

void displayArr(string arr)
{
    cout << "Displaying array..." << endl;
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        cout << arr[i];
    }
    cout << endl
         << "Array displayed..." << endl;
}

int main()
{
    int tc;
    cin >> tc;

    for (int i = 0; i < tc; i++)
    {
        cout << "Case " << i + 1 << endl;

        string str;
        cin >> str;
        displayArr(str);
        char alphabet[26] =
            {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        for (int j = 0; j < str.size(); j++)
        {
            char c = str[j];
            if (c >= 'A' && c <= 'Z')
            {
                c += 32;
            }
            if (c >= 'a' && c <= 'z')
            {
                alphabet[c - 97] = 48;
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
            cout << "missing ";
            for (int j = 0; j < missing; j++)
            {
                cout << missing_letters[j];
            }
            cout << endl;
        }
    }
    return 0;
}