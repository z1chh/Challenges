#include <iostream>
#include <algorithm>

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
void t1();
void test();
void t2();
void t3();

int main()
{
    t3();
    return 0;
}

void t3()
{
    int arr[] = {5, 4, 3, 2, 1};
    sort(arr, arr + 5);
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void t2h(int *arr)
{
    arr[0] = 5;
    arr[1] = 6;
}

void t2()
{
    int arr[2] = {1, 2};
    cout << arr[0] << endl;
    cout << arr[1] << endl;
    t2h(arr);
    cout << arr[0] << endl;
    cout << arr[1] << endl;
}

void t1helper(int *a)
{
    ++*a;
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