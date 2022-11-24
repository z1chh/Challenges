import math


def getDistance(p1, p2, p3):
    # Detuple points and get max and mins
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    max_y, min_y = max(y2, y3), min(y2, y3)
    max_x, min_x = max(x2, x3), min(x2, x3)

    # Maths are legit really fun
    x = y2 - y3
    y = x3 - x2
    z = x * x2 - y * y2
    k = float(math.pow(x, 2) + math.pow(y, 2))
    d = abs(x * x1 + y * y1 + z) / math.sqrt(k)

    px = (y * (y * x1 - x * y1) - x * z)/k
    py = (x * (-1.0 * y * x1 + x * y1) - y * z)/k
    if max_y >= py >= min_y and max_x >= px >= min_x:
        return d / 2.

    d1 = math.sqrt(math.pow(y2 - y1, 2) + math.pow((x2 - x1), 2))
    d2 = math.sqrt(math.pow(y3 - y1, 2) + math.pow((x3 - x1), 2))
    return min(d1, d2) / 2.


def rafting(inner_points, outer_points, n):
    # Set radius to 0
    min_radius = 0
    first = True

    # Get distance
    for i in range(n):
        for p1 in inner_points:
            p2 = outer_points[i]
            p3 = outer_points[i - 1]
            radius = getDistance(p1, p2, p3)

            # Update radius
            if first:
                min_radius += radius
                first = False
            elif radius < min_radius:
                min_radius = radius

    # Return radius
    return min_radius


def main():
    # For each test case
    for _ in range(int(input())):
        # Get inner polygon
        inner_sides = int(input())
        inner_points = []
        for _ in range(inner_sides):
            x, y = map(int, input().split())
            inner_points.append((x, y))

        # Get outer polygon
        outer_sides = int(input())
        outer_points = []
        for _ in range(outer_sides):
            x, y = map(int, input().split())
            outer_points.append((x, y))

        # Solve
        print(rafting(inner_points, outer_points, outer_sides))


if __name__ == "__main__":
    main()
