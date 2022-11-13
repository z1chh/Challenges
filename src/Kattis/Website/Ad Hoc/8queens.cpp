#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

typedef long long ll;
using namespace std;

int main()
{
    ll i, j, k;

    ll totalQueens = 0;
    vector<string> board(8);
    vector<bool> upRight(14, false);
    vector<bool> upLeft(14, false);
    vector<bool> row(8, false);
    vector<bool> col(8, false);

    bool valid = true;

    for (i = 0; i < 8; i++)
    {
        cin >> board[i];
    }

    for (auto s : board)
    {
        for (auto c : s)
        {
            if (c == '*')
            {
                totalQueens++;
            }
        }
    }

    if (totalQueens != 8)
    {
        valid = false;
    }

    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            if (board[i][j] == '*')
            {
                if (!upRight[i + j])
                {
                    upRight[i + j] = true;
                }
                else
                {
                    valid = false;
                }
                if (!row[i])
                {
                    row[i] = true;
                }
                else
                {
                    valid = false;
                }
                if (!col[j])
                {
                    col[j] = true;
                }
                else
                {
                    valid = false;
                }
            }
        }
    }

    for (i = 0; i < 8; i++)
    {
        reverse(board[i].begin(), board[i].end());
    }

    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            if (board[i][j] == '*')
            {
                if (!upLeft[i + j])
                {
                    upLeft[i + j] = true;
                }
                else
                {
                    valid = false;
                }
            }
        }
    }

    if (!valid)
    {
        cout << "invalid" << endl;
    }
    else
    {
        cout << "valid" << endl;
    }

    return 0;
}
