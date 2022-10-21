# Functions
def getBuildingsDestroyed(height, is_left):
    size = len(height)
    buildings_destroyed = 1
    idx = 0 if is_left else size - 1
    cur_building = height[idx]
    while idx < size - 1 if is_left else idx > 0:
        if is_left and height[idx + 1] > cur_building:
            pass


def getMinBlows(height, min_blows):
    while (size := len(height)) > 0:
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

        if left > right:
            pass
        elif left < right:
            pass
        else:
            # left == right
            pass

    return min_blows


if __name__ == '__main__':
    height = list(map(int, input().split()))
    print(getMinBlows(height, 0))
