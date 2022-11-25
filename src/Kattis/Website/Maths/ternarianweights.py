from math import pow


# Get powers of 3 to include 10e9
POWERS_OF_THREE = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147,
                   531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]


def getUpperPow(n):
    power = 0
    value = 1
    while value < n:
        value *= 3
        power += 1
    return power, value


def getLowerPow(n):
    power = 0
    value = 1
    while value <= n:
        value *= 3
        power += 1
    if value == 1:
        return 0, 1
    return power - 1, int(value / 3)


def ternarianWeights(n):
    # Base case
    if n == 0:
        return [], []

    power, value = getUpperPow(n)
    remaining = value - n

    # Get left side weights
    left = []
    while remaining > 0:
        _, newVal = getLowerPow(remaining)
        left.append(newVal)
        remaining -= newVal

    return sorted(left, reverse=True), [value]


def main():
    for _ in range(int(input())):
        left, right = ternarianWeights(int(input()))
        print("left pan:", " ".join(map(str, left)))
        print("right pan:", " ".join(map(str, right)))
        print()


if __name__ == '__main__':
    main()
