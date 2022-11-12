#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    // Get input
    int iterations;
    cin >> iterations;

    // Compute and output result
    cout << pow(pow(2, iterations) + 1, 2) << endl;
    
    // Successful return
    return 0;
}
