#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<char, int> letters;
    string s;
    cin >> s;

    // Count each letter
    for (auto &c : s)
    {
        if (letters.count(c))
            letters[c]++;
        else
            letters[c] = 1;
    }

    // Increase count when odd num of a letter
    int count = 0;
    for (const auto &c : letters)
    {
        if (c.second & 1)
            count++;
    }

    if (count - 1 > 0)
        cout << count - 1;
    else
        cout << '0';
    return 0;
}
