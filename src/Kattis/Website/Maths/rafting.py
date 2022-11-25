import sys
import math

test_cases = int(input())

for i in range(test_cases):
    coordinates_inner = list()
    coordinates_outer = list()

    n_inner = int(input())
    for _ in range(n_inner):
        x, y = list(map(int, input().split()))
        coordinates_inner.append((x, y))

    n_outer = int(input())
    for _ in range(n_outer):
        x, y = list(map(int, input().split()))
        coordinates_outer.append((x, y))

    smallest_distance = sys.maxsize

    for i in range(len(coordinates_outer)):
        x1, y1 = coordinates_outer[i]
        x2, y2 = 0, 0
        if i == len(coordinates_outer)-1:
            x2, y2 = coordinates_outer[0]
        else:
            x2, y2 = coordinates_outer[i+1]

        for j in range(len(coordinates_inner)):
            x3, y3 = coordinates_inner[j]

            outerline_length = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
            u = ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/math.pow(outerline_length, 2)
            projection_x = x1+u*(x2-x1)
            projection_y = y1+u*(y2-y1)

            projection_distance = math.sqrt(
                math.pow(x3-projection_x, 2)+math.pow(y3-projection_y, 2))

            if projection_distance < 1e-9:
                projection_distance = sys.maxsize
            elif math.sqrt(math.pow(projection_x-x1, 2)+math.pow(projection_y-y1, 2))+math.sqrt(math.pow(projection_x-x2, 2)+math.pow(projection_y-y2, 2))-math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2)) > 1e-9:
                projection_distance = sys.maxsize

            d1 = math.sqrt(math.pow(x3-x1, 2)+math.pow(y3-y1, 2))
            d2 = math.sqrt(math.pow(x3-x2, 2)+math.pow(y3-y2, 2))

            current_distance = min(d1, d2, projection_distance)

            if current_distance < smallest_distance:
                smallest_distance = current_distance

    print(smallest_distance/2.0)
