#include <iostream>

using namespace std;

int main()
{
    int size, cur_el;
    cin >> size;
    int arr[size];
    for (int i = size - 1; i >= 0; i--)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
