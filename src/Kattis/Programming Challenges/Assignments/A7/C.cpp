#include <iostream>
#include <map>
#include <vector>

using namespace std;

void update_ratings(map<int, int> *movie_ratings, int ID1, int ID2, int rating1, int rating2, map<int, vector<int>> *similarities);

int main()
{
    // Get input
    int n, h, l, best_rating = -1, best_ID = 1001;
    cin >> n >> h >> l;
    map<int, vector<int>> similarities;

    // Initialize movie_ratings
    map<int, int> movie_ratings;
    for (int i = 0; i < n; i++)
    {
        movie_ratings[i] = INT_MAX;
    }

    // Get horror list
    int horror_movie_ID;
    for (int i = 0; i < h; i++)
    {
        cin >> horror_movie_ID;
        movie_ratings[horror_movie_ID] = 0;
    }

    int ID1, ID2, rating1, rating2;
    for (int i = 0; i < l; i++)
    {
        cin >> ID1 >> ID2;

        // Update similar movies
        similarities[ID1].push_back(ID2);
        similarities[ID2].push_back(ID1);

        // Get ratings
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
        update_ratings(&movie_ratings, ID1, ID2, rating1, rating2, &similarities);
        /* cout << "IDS " << ID1 << " " << ID2 << endl;
        for (auto r : movie_ratings)
        {
            cout << r.first << " has value " << r.second << endl;
        } */
    }

    for (auto const &x : movie_ratings)
    {
        if (x.second > best_rating)
        {
            best_rating = x.second;
            best_ID = x.first;
        }
        else if (x.second == best_rating)
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

void update_ratings(map<int, int> *movie_ratings, int ID1, int ID2, int rating1, int rating2, map<int, vector<int>> *similarities)
{
    if (rating1 == 0 && rating2 != 0)
    {
        (*movie_ratings)[ID2] = 1;
    }
    else if (rating2 == 0 && rating1 != 0)
    {
        (*movie_ratings)[ID1] = 1;
    }
    else if (rating2 != 0 && rating1 != 0)
    {
        if (rating1 < rating2)
        {
            (*movie_ratings)[ID2] = (*movie_ratings)[ID1] + 1;
        }
        else if (rating1 > rating2)
        {
            (*movie_ratings)[ID1] = (*movie_ratings)[ID2] + 1;
        }
    }
}
