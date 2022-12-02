def aPrizeNoOneCanWin(numItems, maxCost, items):
    # Check if only one item
    if numItems == 1:
        return 1

    # Sort items by price ascending
    items.sort()

    # Check if two consecutive items exceed the max cost
    for i in range(numItems - 1):
        if items[i] + items[i + 1] > maxCost:
            return i + 1

    # Otherwise, all items can be used
    return numItems


def main():
    # Get input
    n, X = map(int, input().split())
    items = list(map(int, input().split()))

    # Compute and output answer
    print(aPrizeNoOneCanWin(n, X, items))


if __name__ == "__main__":
    main()
