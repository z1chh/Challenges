#include <iostream>
#include <vector>

using namespace std;

void t1();
void t2();
void t3();
void t4();

int main()
{
    t4();
    return 0;
}

void t1()
{
    vector<vector<int>> v;
    vector<int> a;
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    a.push_back(4);
    v.push_back(a);
    a.clear();
    a.push_back(5);
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    v.push_back(a);

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}

void t2()
{
    vector<vector<int>> v;
    vector<int> a;
    a.push_back(1);
    a.push_back(2);
    v.push_back(a);
    a.clear();
    a.push_back(2);
    a.push_back(1);
    v.push_back(a);
    a.clear();
    a.push_back(5);
    a.push_back(2);
    v.push_back(a);
    a.clear();
    a.push_back(2);
    a.push_back(5);
    v.push_back(a);

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}

void t3()
{
    vector<vector<int>> v;
    vector<int> a;
    a = {36, 59, 71, 15, 26, 82, 87};
    v.push_back(a);
    a.clear();
    a = {56, 36, 59, 71, 15, 26, 82};
    v.push_back(a);
    a.clear();
    a = {15, 0, 36, 59, 71, 15, 26};
    v.push_back(a);

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}

void t4()
{
    vector<int> a;
    a = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    for (int j = 0; j < a.size(); j++)
    {
        cout << a[j] << " ";
    }
    cout << endl;
}