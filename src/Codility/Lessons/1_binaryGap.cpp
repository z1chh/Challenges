#include <iostream>

using namespace std;

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int N) {
    // write your code in C++14 (g++ 6.2.0)
    int largest = 0, remainder, curGap = 0;
    bool surrounded = false;

    while (N > 0)
    {
        remainder = N & 1;
        if (remainder == 1)
        {
            // If previously encountered a 1-bit, check for binary gap
            if (surrounded)
            {
                // Update largest binary gap if necessary
                if (curGap > largest)
                {
                    largest = curGap;
                }
            }

            // Reset the current binary gap
            curGap = 0;

            // To check if we already encountered a 1-bit
            surrounded = true;
        }
        else
        {
            // Increment current binary gap
            curGap++;
        }

        // SRL to get next bit
        N = N >> 1;
    }

    // Return the largest binary gap
    return largest;
}

// To remove
int main()
{
    cout << solution(9) << endl;
}