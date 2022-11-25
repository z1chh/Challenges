"""
Grid:
+---+---+---+
| 0 | 1 | 2 |
+---+---+---+
| 3 | 4 | 5 |
+---+---+---+
| 6 | 7 | 8 |
+---+---+---+
"""


# Tiles to flip in function of the chosen tile
neighbors = {0: {0, 1, 3},
             1: {0, 1, 2, 4},
             2: {1, 2, 5},
             3: {0, 3, 4, 6},
             4: {1, 3, 4, 5, 7},
             5: {2, 4, 5, 8},
             6: {3, 6, 7},
             7: {4, 6, 7, 8},
             8: {5, 7, 8}}


def flipBoard(board, n):
    # Convert into a list
    newBoard = [c for c in board]

    # Flip the correponding tiles
    for v in neighbors[n]:
        if newBoard[v] == "*":
            newBoard[v] = "."
        else:
            newBoard[v] = "*"

    # Return as string
    return ''.join(newBoard)


# Stringify the board (for debugging purposes)
def boardAsString(board):
    return (f"+---+---+---+\n" +
            f"| {board[0]} | {board[1]} | {board[2]} |\n" +
            f"+---+---+---+\n" +
            f"| {board[3]} | {board[4]} | {board[5]} |\n" +
            f"+---+---+---+\n" +
            f"| {board[6]} | {board[7]} | {board[8]} |\n" +
            f"+---+---+---+")


def flipFive(goalBoard):
    # Storing played boards and their score
    played = set()
    played.add(".........")
    storage = dict()
    storage["........."] = 0

    # Initialize queue with whiteboard
    queue = ["........."]

    # Exhaustive search
    winScores = set()
    while queue:
        # Pop the board from the queue and retrieve its score
        poppedBoard = queue.pop(0)
        curScore = storage[poppedBoard]

        # Get every possible move
        for i in range(9):
            flippedBoard = flipBoard(poppedBoard, i)

            # Check if it is a winning board
            if flippedBoard == goalBoard:
                winScores.add(curScore + 1)
                # print(boardAsString(poppedBoard))
                # print(boardAsString(flippedBoard))
                #print("score of", curScore + 1)

            # Check if not visited already
            elif flippedBoard not in played or storage[flippedBoard] > curScore + 1:
                played.add(flippedBoard)
                queue.append(flippedBoard)
                storage[flippedBoard] = curScore + 1

    # Return minimum number of moves
    return min(winScores)


def main():
    # For each test case
    for _ in range(int(input())):
        # Get input
        goalBoard = ""
        for _ in range(3):
            goalBoard += input()

        # Compute and output score
        print(flipFive(goalBoard))


if __name__ == '__main__':
    main()
