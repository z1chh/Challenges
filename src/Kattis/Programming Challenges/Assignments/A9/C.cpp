#include <iostream>
#include <cmath>

using namespace std;

float segmentLength(int x1, int y1, int x2, int y2);
float getSlope(int x1, int y1, int x2, int y2);
void getLastCorner(float hypothenuse, float slope, int x, int y);

int main()
{
    // Get input
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    // Compute hypothenuse
    float d1, d2, d3, hypothenuse;
    d1 = segmentLength(x1, y1, x2, y2);
    d2 = segmentLength(x1, y1, x3, y3);
    d3 = segmentLength(x2, y2, x3, y3);
    hypothenuse = max(d1, d2);
    hypothenuse = max(hypothenuse, d3);

    // Compute last corner
    if (hypothenuse == d1)
    {
        getLastCorner(hypothenuse, getSlope(x1, y1, x2, y2), x3, x3);
    }
    else if (hypothenuse == d2)
    {
        getLastCorner(hypothenuse, getSlope(x1, y1, x3, y3), x2, x2);
    }
    else
    {
        getLastCorner(hypothenuse, getSlope(x2, y2, x3, y3), x1, x1);
    }

    // Successful return
    return 0;
}

float segmentLength(int x1, int y1, int x2, int y2)
{
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

float getSlope(int x1, int y1, int x2, int y2)
{
    float toReturn = y2 - y1;
    toReturn /= x2 - x1;
    return toReturn;
}

void getLastCorner(float hypothenuse, float slope, int x, int y)
{
    float newSlope = -1 / slope;
    cout << hypothenuse << " " << slope << " " << newSlope << endl;
    int xc, yc;

    // Check if third point below or above slope
    if (y < x * slope)
    {
        // Below
        cout << "below" << endl;
    }
    else
    {
        // Above
        xc = x + y * newSlope;
        yc = y + x * newSlope;
        cout << "above" << endl;
    }

    // Output last corner
    cout << xc << " " << yc << endl;
}
