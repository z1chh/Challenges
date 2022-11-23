def sol(length):
    if length == 0:
        return 1
    elif length == 1:
        return 1
    elif length == 2:
        return 2
    elif length == 3:
        return 4
    ways = [1, 2, 4]
    for _ in range(length - 3):
        ways.append(ways[-1] + ways[-2] + ways[-3])
    return ways[-1]


def main():
    print(sol(int(input())))


if __name__ == '__main__':
    main()
