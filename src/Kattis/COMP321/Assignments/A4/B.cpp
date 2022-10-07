#include <iostream>

using namespace std;

int main()
{
    // Declare variables
    int num_rocks, num_moves, move;

    // Get input
    while (cin >> num_rocks >> num_moves)
    {
        // Get moves
        int moves[num_moves];
        for (int i = 0; i < num_moves; i++)
        {
            cin >> moves[i];
        }

        // Initialize boolean array
        bool win[num_rocks + 1];
        for (int i = 0; i < num_rocks + 1; i++)
        {
            win[i] = false;
        }

        // Populate array
        for (int i = 1; i < num_rocks + 1; i++)
        {
            for (int j = 0; j < num_moves; j++)
            {
                move = moves[j];
                if ((i - move >= 0) && !win[i - move])
                {
                    win[i] = true;
                    break;
                }
            }
        }

        // Output result
        if (win[num_rocks])
        {
            cout << "Stan wins" << endl;
        }
        else
        {
            cout << "Ollie wins" << endl;
        }
    }

    // Successful return
    return 0;
}
