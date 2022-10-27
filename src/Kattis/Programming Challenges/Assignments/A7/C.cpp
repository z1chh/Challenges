#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main()
{
    // Get input
    int n, h, l, horror_movie_ID;
    cin >> n >> h >> l;
    int horror_movies[h];
    map<int, vector<int>> similarities;
    for (int i = 0; i < h; i++)
    {
        cin >> horror_movie_ID;
        horror_movies[i] = horror_movie_ID;
        similarities[horror_movie_ID] = vector<int>();
    }

    for (int i = 0; i < l; i++)
    {
        // TODO
    }

    // LOGIC

    // Successful return
    return 0;
}