#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int dist(double x, double y);

int main()
{
    // Get number of test cases
    int num_cases, num_commands, value;
    string command_type;
    double angle, degrees, distance, x, y, PI = 3.141592653589793238462643383;
    cin >> num_cases;

    for (int i = 0; i < num_cases; i++)
    {
        // Get number of commands
        cin >> num_commands;
        pair<string, double> commands[num_commands];

        // Get each command
        for (int j = 0; j < num_commands; j++)
        {
            cin >> command_type >> value;
            commands[j] = make_pair(command_type, value);
        }

        // Compute final location
        angle = 0.;
        x = 0.;
        y = 0.;
        for (const auto &[cmd, v] : commands)
        {
            if (cmd == "fd")
            {
                x += sin(angle * (PI / 180)) * v;
                y += cos(angle * (PI / 180)) * v;
            }
            if (cmd == "bk")
            {
                x -= sin(angle * (PI / 180)) * v;
                y -= cos(angle * (PI / 180)) * v;
            }
            if (cmd == "lt")
            {
                angle += v;
            }
            if (cmd == "rt")
            {
                angle -= v;
            }
        }

        // Output final distance
        cout << dist(x, y) << endl;
    }

    // Successful return
    return 0;
}

int dist(double x, double y)
{
    double total = pow(x, 2) + pow(y, 2);
    total = sqrt(total);
    return round(total);
}
