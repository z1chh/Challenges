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
    newBoard = [c for c in board]
    for v in neighbors[n]:
        if newBoard[v] == "*":
            newBoard[v] = "."
        else:
            newBoard[v] = "*"
    return ''.join(newBoard)


def isWinningBoard(board):
    for c in board:
        if c == "*":
            return False
    return True


def boardAsString(board):
    print(
        f"-------\n|{board[0]} {board[1]} {board[2]}|\n|{board[3]} {board[4]} {board[5]}|\n|{board[6]} {board[7]} {board[8]}|\n-------")


# For each test case
for _ in range(int(input())):
    # Get input
    goalBoard = ""
    for _ in range(3):
        goalBoard += input()

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
        poppedBoard = queue.pop(0)
        # print("popping:")
        # boardAsString(poppedBoard)
        curScore = storage[poppedBoard]
        for i in range(9):
            flippedBoard = flipBoard(poppedBoard, i)
            if flippedBoard == goalBoard:
                winScores.add(curScore + 1)
            elif flippedBoard not in played:
                # print(f"adding to queue ({i}):")
                # boardAsString(flippedBoard)
                queue.append(flippedBoard)
                played.add(flippedBoard)
                if flippedBoard in storage:
                    storage[flippedBoard] += 1
                else:
                    storage[flippedBoard] = 1
    print(min(winScores))
