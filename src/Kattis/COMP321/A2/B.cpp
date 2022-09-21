#include <iostream>

using namespace std;

int main() {
    // Declare vars
    string input;
    char output[1000000];
    int index = 0;
    char c;

    // Get input
    cin >> input;

    // Format input
    for (int i = 0; i < input.length(); i++) {
        c = input.at(i);
        if (c >= 'a') {
            output[index++] = c;
        } else {
            index--;
        }
    }

    // Print output
    for (int i = 0; i < index; i++) {
        cout << output[i];
    }

    // Exit
    return 0;
}
