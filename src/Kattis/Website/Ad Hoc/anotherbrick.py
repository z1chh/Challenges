def anotherbrick(h, w, bricks):
    # Initialize current row and height
    curW = 0
    curH = 0

    # Check if each brick fits
    for brick in bricks:
        # Place brick
        curW += brick
        
        # Check if annoyed
        if curW > w:
            return "NO"

        # Check if go next row
        if curW == w:
            curW = 0
            curH += 1

        # Check if wall completed
        if curH == h:
            return "YES"

    # Wall not completed
    return "NO"


def main():
    # Get input
    h, w, _ = map(int, input().split())
    bricks = map(int, input().split())

    # Compute and output answer
    print(anotherbrick(h, w, bricks))


if __name__ == "__main__":
    main()
