#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    // Declare vars
    int num_words, num_jobs, price, salary;
    string word;
    cin >> num_words >> num_jobs;
    map<string, int> hay_points;

    // Get words that give hay points
    for (int i = 0; i < num_words; i++) {
        cin >> word >> price;
        hay_points[word] = price;
    }

    // Compute salary for each job
    for (int i = 0; i < num_jobs; i++) {
        salary = 0;
        cin >> word;
        while (word != ".") {
            if (hay_points.count(word) == 1) {
                salary += hay_points[word];
            }
            cin >> word;
        }
        cout << salary << endl;
    }

    // Successful return
    return 0;
}
