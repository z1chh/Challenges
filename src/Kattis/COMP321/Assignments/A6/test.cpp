#include <iostream>

using namespace std;

int student_id = 0;

class Student
{
public:
    string name;

    Student(string name) : name(name)
    {
    }

    void print_name()
    {
        cout << "Student name is " << name << endl;
    }
};
// Functions
void hello();
void t1helper();
void t1();
void test();

int main()
{
    t1();
    return 0;
}

void t1helper(int *a)
{
    ++a;
}

void t1()
{
    int a = 5;
    cout << a << endl;
    t1helper(&a);
    cout << a << endl;
    t1helper(&a);
    cout << a << endl;
}

void hello()
{
    cout << "Hello World!" << endl;
}

void test()
{
    Student s = Student("Zichh");
    s.print_name();
    Student s2("Stub");
    s2.print_name();
}