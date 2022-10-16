#include <iostream>

using namespace std;

int main() {
    // Declare vars
    int max_operations = 0, register_value;

    // Register values
    int register_max[] = {1, 2, 4, 6, 10, 12, 16, 18};
    int register_ops[] = {1, 2, 6, 30, 210, 2310, 30030, 510510};
    for (int i = 0; i < 8; i++) {
        cin >> register_value;
        max_operations += (register_max[i] - register_value) * register_ops[i];
    }
    cout << max_operations << endl;
}
