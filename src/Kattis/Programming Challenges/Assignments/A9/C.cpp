#include <iostream>
#include <cmath>

using namespace std;

float segmentLength(int x1, int y1, int x2, int y2);
pair<float, float> getMiddle(int x1, int y1, int x2, int y2);
pair<float, float> getLastCorner(pair<float, float> middle, int x, int y);

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
    hypothenuse = max(max(d1, d2), d3);

    // Compute last corner
    pair<float, float> lastCorner;
    if (hypothenuse == d1)
    {
        lastCorner = getLastCorner(getMiddle(x1, y1, x2, y2), x3, y3);
    }
    else if (hypothenuse == d2)
    {
        lastCorner = getLastCorner(getMiddle(x1, y1, x3, y3), x2, y2);
    }
    else
    {
        lastCorner = getLastCorner(getMiddle(x2, y2, x3, y3), x1, y1);
    }

    // Output result
    cout << lastCorner.first << " " << lastCorner.second << endl;

    // Successful return
    return 0;
}

float segmentLength(int x1, int y1, int x2, int y2)
{
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

pair<float, float> getMiddle(int x1, int y1, int x2, int y2)
{
    return make_pair((x1 + x2) / 2., (y1 + y2) / 2.);
}

pair<float, float> getLastCorner(pair<float, float> middle, int x, int y)
{
    float xl, yl;
    xl = middle.first * 2 - x;
    yl = middle.second * 2 - y;
    return make_pair(xl, yl);
}
