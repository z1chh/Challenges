#include <iostream>
#include <string>

using namespace std;

int main()
{
    string pattern, text;
    int pattern_size, text_size, position, index_str;
    while (getline(std::cin, pattern))
    {
        getline(std::cin, text);
        pattern_size = pattern.size();
        text_size = text.size();
        position = 0;

        while (true)
        {
            index_str = text.find(pattern, position);
            if (index_str != string::npos)
            {
                cout << index_str << " ";
            }
            if (++position == text_size)
            {
                break;
            }
        }
        cout << endl;
    }

    // Successful return
    return 0;
}
