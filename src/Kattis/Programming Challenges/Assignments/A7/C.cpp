#include <iostream>
#include <map>
#include <vector>

using namespace std;

void update_ratings(map<int, int> *movie_ratings, int ID1, int ID2, int rating1, int rating2);

int main()
{
    // Get input
    int n, h, l, horror_movie_ID, ID1, ID2, rating1, rating2, best_rating, best_ID = 1001;
    cin >> n >> h >> l;
    best_rating = INT_MAX;
    map<int, int> movie_ratings;
    map<int, vector<int>> similarities;
    for (int i = 0; i < h; i++)
    {
        cin >> horror_movie_ID;
        movie_ratings[horror_movie_ID] = 0;
    }

    for (int i = 0; i < l; i++)
    {
        cin >> ID1 >> ID2;
        if (movie_ratings.count(ID1) == 1)
        {
            rating1 = movie_ratings[ID1];
        }
        else
        {
            rating1 = -1;
        }
        if (movie_ratings.count(ID2) == 1)
        {
            rating2 = movie_ratings[ID2];
        }
        else
        {
            rating2 = -1;
        }
        update_ratings(&movie_ratings, ID1, ID2, rating1, rating2);
    }

    for (auto const &x: movie_ratings)
    {
        if (x.second <= best_rating)
        {
            best_rating = x.second;
            if (x.first < best_ID)
            {
                best_ID = x.first;
            }
        }
    }

    // Output movie with highest Horror Index
    cout << best_ID << endl;

    // Successful return
    return 0;
}

void update_ratings(map<int, int> *movie_ratings, int ID1, int ID2, int rating1, int rating2)
{
    // TODO
}
