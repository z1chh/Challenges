#include <iostream>

using namespace std;

void increment(int *i)
{
    (*i)++;
}

int javaIncrement(int a)
{
    return ++a;
}

int main()
{
    // C++
    int a = 5;
    increment(&a);
    cout << a << endl;

    // JAVA
    int b = 10;
    b = javaIncrement(b);
    cout << b << endl;
}