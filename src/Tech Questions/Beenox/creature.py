# Functions
def getBuildingsDestroyed(height):
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

    return left, right


def getMinBlows(height, min_blows):
    left, right = getBuildingsDestroyed(height)

    return min_blows


if __name__ == '__main__':
    height = list(map(int, input().split()))
    print(getMinBlows(height, 0))
