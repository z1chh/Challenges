# Functions
def getBuildingsDestroyedPerSide(height):
    size = len(height)
    left = 1
    left_el = height[0]
    for i in range(1, size):
        if height[i] > left_el:
            left_el = height[i]
            left += 1
        else:
            break

    right = 1
    right_el = height[-1]
    for i in range(size - 2, -1, -1):
        if height[i] > right_el:
            right_el = height[i]
            right += 1
        else:
            break

    #print("Buildings:", height, "\nLeft and right values:", left, right)
    return left, right


def destroyBuildings(height, num_buildings, side):
    if side == 0:
        for _ in range(num_buildings):
            height.pop(0)
    else:
        for _ in range(num_buildings):
            height.pop()


def getMinBlows(height, min_blows):
    # Return number of blows if height is empty
    if not height:
        return min_blows

    # Check which side destroys the most buildings
    left, right = getBuildingsDestroyedPerSide(height)
    if left > right:
        destroyBuildings(height, left, 0)
        return getMinBlows(height, min_blows + 1)
    elif left < right:
        destroyBuildings(height, right, 1)
        return getMinBlows(height, min_blows + 1)
    else:
        left_copy = height.copy()
        right_copy = height.copy()
        destroyBuildings(left_copy, left, 0)
        destroyBuildings(right_copy, right, 1)
        return 1 + min(getMinBlows(left_copy, min_blows), getMinBlows(right_copy, min_blows))


if __name__ == '__main__':
    """ height = list(map(int, input().split()))
    print(getMinBlows(height, 0)) """
    print(getMinBlows([1, 2, 3, 4, 3, 2, 3, 2, 1], 0))
    print(getMinBlows([1, 2, 3, 4, 8, 7, 6, 5], 0))
    print(getMinBlows([2, 1, 2], 0))
    print(getMinBlows([1, 2, 1, 2, 10, 9], 0))
    print(getMinBlows([22, 75, 26, 45, 72, 81, 47, 29, 97, 2, 75, 25, 82, 84, 17, 56, 32, 2, 28, 37, 57, 39, 18,
          11, 79, 6, 40, 68, 68, 16, 40, 63, 93, 49, 91, 10, 55, 68, 31, 80, 57, 18, 34, 28, 76, 55, 21, 80, 22, 45], 0))
