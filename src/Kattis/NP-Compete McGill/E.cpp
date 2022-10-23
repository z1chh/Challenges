#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    double gx, gy, dx, dy, hx, hy, geuc, deuc, sx, sy;
    bool escape = false;
    cin >> gx >> gy >> dx >> dy;
    vector<pair<double, double>> holes;
    while (cin >> hx >> hy)
    {
        holes.push_back(make_pair(hx, hy));
    }
    for (auto it = holes.begin(); it != holes.end(); it++)
    {
        hx = it->first;
        hy = it->second;
        geuc = sqrt(pow(gx - hx, 2) + pow(gy - hy, 2));
        deuc = sqrt(pow(dx - hx, 2) + pow(dy - hy, 2));
        if (geuc * 2 <= deuc)
        {
            escape = true;
            sx = hx;
            sy = hy;
            break;
        }
    }
    if (escape)
    {
        printf("The gopher can escape through the hole at (%.3f,%.3f).", sx, sy);
    }
    else
    {
        cout << "The gopher cannot escape." << endl;
    }
    return 0;
}
