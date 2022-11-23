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
neighbors = {0: {0, 1, 3}, 1: {0, 1, 2, 4}, 2: {1, 2, 5}, 3: {0, 3, 4, 6}, 4: {
    1, 3, 4, 5, 7}, 5: {2, 4, 5, 8}, 6: {3, 6, 7}, 7: {4, 6, 7, 8}, 8: {5, 7, 8}}


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


# For each test case
for _ in range(int(input())):
    # Get input
    goalBoard = ""
    for _ in range(3):
        goalBoard += input()

    # Storing played boards
    played = set()
    played.add(".........")
    queue = dict()
    queue["........."] = 0

    # Exhaustive search
    winScores = []
    while queue:
        poppedBoard, curScore = queue.pop()
        for i in range(9):
            flippedBoard = flipBoard(poppedBoard, i)
            if flippedBoard == goalBoard:
                winScores.append(curScore)
            elif flippedBoard not in played:
                queue.append((flippedBoard, curScore + 1))
    print(max(winScores))
