#include <iostream>
#include <string>

using namespace std;

bool erase(string orig, string deleted, int val)
{

    if (val % 2 == 0)
    {
        return orig == deleted;
    }
    else
    {
        for (int i = 0; i < orig.size(); i++)
        {
            if (orig[i] == deleted[i])
            {
                return false;
            }
        }
        return true;
    }
}

int main()
{
    int val;
    cin >> val;
    cin.ignore();

    string orig, deleted;
    getline(cin, orig);
    getline(cin, deleted);
    if (erase(orig, deleted, val))
    {
        cout << "Deletion succeeded" << endl;
    }
    else
    {
        cout << "Deletion failed" << endl;
    }
    return 0;
}
