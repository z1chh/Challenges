# Functions
def getBuildingsDestroyedPerSide(height):
    size = len(height)
    left = 1
    left_el = height[0]
    while left < size:
        if height[left] > left_el:
            left_el = height[left]
            left += 1
        else:
            break

    right = 1
    right_el = height[-1]
    while size - 1 - right >= 0:
        if height[right] > right_el:
            right_el = height[right]
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
    height = list(map(int, input().split()))
    print(getMinBlows(height, 0))
