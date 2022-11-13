#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int cases, students, grade, aboveAvg;
    float avg;
    vector<int> grades;
    cin >> cases;
    for (int i = 0; i < cases; i++)
    {
        cin >> students;
        avg = 0;
        aboveAvg = 0;
        grades.clear();
        for (int j = 0; j < students; j++)
        {
            cin >> grade;
            avg += grade;
            grades.push_back(grade);
        }
        avg /= students;
        for (int g : grades)
        {
            if (g > avg)
            {
                aboveAvg++;
            }
        }
        printf("%.3f%\n", float(aboveAvg) * 100 / students);
    }
    return 0;
}
