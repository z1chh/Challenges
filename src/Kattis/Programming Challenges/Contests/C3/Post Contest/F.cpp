#include <iostream>

using namespace std;

int main()
{
    // Get input
    int numTasks, timeLimit, completedTasks = 0, curTime = 0, curTaskTime;
    cin >> numTasks >> timeLimit;

    // Do task while time limit not exceeded
    for (int i = 0; i < numTasks; i++)
    {
        cin >> curTaskTime;
        if (curTime + curTaskTime > timeLimit)
        {
            break;
        }
        curTime += curTaskTime;
        completedTasks++;
    }

    // Output results
    cout << completedTasks << endl;

    // Successful return
    return 0;
}
