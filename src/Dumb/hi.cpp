#include <iostream>
#include <map>
#include <string>

using namespace std;

void increment(int *i);

int javaIncrement(int a);

void t1();
void t2();

int main()
{
    t2();
}

void t2()
{
    map<int, pair<string, int>> m;
    m[0] = make_pair("Hello", 5);
    m[1] = make_pair("World!", 10);
    // it points to nothing at first, then everytime you it++ it points to next element
    // {1, 2, 3, 4, 5}
    // it -> Nothing, 1, 2, 3, 4, 5, ERR)
    for (auto it = m.begin(); it != m.end(); ++it)
    {
        cout << it->first << "\t" << it->second.first << "\t" << it->second.second << endl;
    }
}

void t1()
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

void increment(int *i)
{
    (*i)++;
}

int javaIncrement(int a)
{
    return ++a;
}
