#include <iostream>
#include <vector>

using namespace std;

void t1();
void t2();
void t3();

int main()
{
    t3();
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
    a.push_back(36);
    a.push_back(59);
    a.push_back(71);
    a.push_back(15);
    a.push_back(26);
    a.push_back(82);
    a.push_back(87);
    v.push_back(a);
    a.clear();
    a.push_back(56);
    a.push_back(36);
    a.push_back(59);
    a.push_back(71);
    a.push_back(15);
    a.push_back(26);
    a.push_back(82);
    v.push_back(a);
    a.clear();
    a.push_back(15);
    a.push_back(0);
    a.push_back(36);
    a.push_back(59);
    a.push_back(71);
    a.push_back(15);
    a.push_back(26);
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