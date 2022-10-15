#include <iostream>

using namespace std;

int student_id = 0;

class Student
{
public:
    string name;
    int id;

    Student(string name) : name(name)
    {
        id = student_id++;
    }

    /* friend ostream &operator<<(ostream &strm, const Student &s)
    {
        return s.name; //+ " (" + s.id + ")";
    } */

    void print_name()
    {
        cout << "Student name is " << name << endl;
    }

    void print_id()
    {
        cout << "Student ID is " << id << endl;
    }
};

void test()
{
    Student s = Student("Zichh");
    s.print_name();
    s.print_id();
    Student s2("Stub");
    s2.print_name();
    s2.print_id();
}

int main()
{
    cout << "Hello World!" << endl;
    return 0;
}