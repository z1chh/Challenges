#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
    // Get number of test cases
    int num_cases, num_segments;
    float angle, degrees, distance, x, y, PI = 2 * acos(0.);
    cin >> num_cases;
    
    for (int i = 0; i < num_cases; i++)
    {
        // Get number of segments
        cin >> num_segments;
        pair<float, float> segments[num_segments];
        
        // Get each segment
        for (int j = 0; j < num_segments; j++)
        {
            cin >> degrees >> distance;
            segments[j] = make_pair(degrees, distance);
        }
        
        // Compute final location
        angle = 0.;
        x = 0.;
        y = 0.;
        for (const auto& [deg, dist]: segments)
        {
            angle += deg;
            x += sin(-angle * (PI / 180)) * dist;
            y += cos(-angle * (PI / 180)) * dist;
        }
        
        // Output final coords
        cout << setprecision(7) << x << " " << y << endl;
        // printf("%.6f %.6f\n", x, y);
    }
    
    // Successful return
    return 0;
}
