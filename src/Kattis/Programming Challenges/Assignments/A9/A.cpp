#include <iostream>
#include <iomanip>

using namespace std;

int within(int x1, int y1, int x2, int y2, int x3, int y3, int tx, int ty);

int main()
{
    // Get input
    int x1, y1, x2, y2, x3, y3, num_trees, tree_x, tree_y;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> num_trees;
    pair<int, int> trees[num_trees];
    for (int i = 0; i < num_trees; i++)
    {
        cin >> tree_x >> tree_y;
        trees[i] = make_pair(tree_x, tree_y);
    }
    
    // Compute triangle area
    float area = abs(x1 * (y2- y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.;
    
    // Compute number of trees belonging to Ante
    int trees_Ante = 0;
    float to_compare;
    for (const auto&[x, y]: trees)
    {
        to_compare = abs(x1 * (y2- y) + x2 * (y - y1) + x * (y1 - y2)) / 2.;
        to_compare += abs(x1 * (y- y3) + x * (y3 - y1) + x3 * (y1 - y)) / 2.;
        to_compare += abs(x * (y2- y3) + x2 * (y3 - y) + x3 * (y - y2)) / 2.;
        if (to_compare == area)
        {
            trees_Ante++;
        }
    }
    
    // Output area of land belonging to Ante
    printf("%.1f\n", area);
    
    // Output number of trees belonging to Ante
    cout << trees_Ante << endl;
    
    // Successful return
    return 0;
}
