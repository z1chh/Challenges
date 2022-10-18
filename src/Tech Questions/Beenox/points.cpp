#include <iostream>
#include <cmath>

using namespace std;

/* Write your class implementations here. */
// Classes
class Point2D
{
public:
    Point2D(int x_param, int y_param) : x_coord(x_param),
                                        y_coord(y_param)
    {
        // Nothing else to do for constructor
    }

    ~Point2D()
    {
        // Nothing particular to do
    }

    double dist2D(Point2D point);
    void printDistance(double d);

    // Protected fields (for Point3D to access them)
protected:
    int x_coord;
    int y_coord;
};

class Point3D : public Point2D
{
public:
    Point3D(int x_param, int y_param, int z_param) : Point2D(x_param, y_param),
                                                     z_coord(z_param)
    {
        // Nothing else to do for constructor
    }

    ~Point3D()
    {
        // Nothing particular to do
    }

    double dist3D(Point3D point);
    void printDistance(double d);

private:
    int z_coord;
};

// Class methods
double Point2D::dist2D(Point2D point)
{
    return sqrt(pow((this->x_coord - point.x_coord), 2) + pow((this->y_coord - point.y_coord), 2));
}

void Point2D::printDistance(double d)
{
    cout << "2D distance = " << ceil(d) << endl;
}

double Point3D::dist3D(Point3D point)
{
    return sqrt(pow((this->x_coord - point.x_coord), 2) + pow((this->y_coord - point.y_coord), 2) + pow((this->z_coord - point.z_coord), 2));
}

void Point3D::printDistance(double d)
{
    // Overrides Point2D::printDistance
    cout << "3D distance = " << ceil(d) << endl;
}

int main()
{
    int x1;
    int y1;
    int z1;
    int x2;
    int y2;
    int z2;

    cin >> x1 >> y1 >> z1;
    cin >> x2 >> y2 >> z2;

    Point3D p1(x1, y1, z1);
    Point3D p2(x2, y2, z2);
    double d2 = p1.dist2D(p2);
    double d3 = p1.dist3D(p2);
    // The code below uses runtime polymorphism to call the overridden printDistance method:
    Point2D p(0, 0);
    p.printDistance(d2);
    p = p1;
    p1.printDistance(d3);

    return 0;
}
