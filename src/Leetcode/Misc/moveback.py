# Helper function to move ith element of the list to the back
def moveBack(l, i):
    for i in range(i, len(l) - 1):
        l[i], l[i + 1] = l[i + 1], l[i]


def main():
    l = [1, 2, 2, 3, 4]
    moveBack(l, 1)
    print(l)


if __name__ == "__main__":
    main()
