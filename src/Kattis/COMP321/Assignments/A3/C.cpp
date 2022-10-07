#include <iostream>

using namespace std;

int main() {
    int numCalls, numIntervals;
    while(true) {
        cin >> numCalls;
        cin >> numIntervals;
        if (numCalls == 0 && numIntervals == 0) {
            break;
        }

        int calls[numCalls][2];
        for (int i = 0; i < numCalls; i++) {
            int start, duration;
            cin >> start; // Ignore source
            cin >> start; // Ignore dest
            cin >> start;
            cin >> duration;
            calls[i][0] = start;
            calls[i][1] = start + duration;
        }

        int operators, cStart, cEnd;
        for (int i = 0; i < numIntervals; i++) {
            int iStart, iDuration;
            cin >> iStart;
            cin >> iDuration;

            operators = 0;

            for (int j = 0; j < numCalls; j++) {
                cStart = calls[j][0];
                cEnd = calls[j][1];
                if (cStart <= iStart && iStart < cEnd) {
                    operators++;
                } else if (iStart <= cStart && cStart < iStart + iDuration) {
                    operators++;
                }
            }
            cout << operators << endl;
        }
    }
    return 0;
}