#include <iostream>

using namespace std;

bool power(int n, string& s) {
    for (int i = n; i < s.size(); i++)
    {
        if (s[i] != s[i-n])
            return false;
    }
    return true;
}

int main() {

    string s;
    while(cin >> s && s != ".")
    {
        int len = s.size();
        for(int i = 1; i <= len; i++)
        {
            if (len % i == 0 && power(i, s))
            {
                cout << len/i << '\n';
                break;
            }
        }
    }
    return 0;
}