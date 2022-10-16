def add_moves(board, queue, bank, nm):
    # Check for possible moves in the board
    for i in range(5):
        for j in range(9):
            pos = board[i][j]
            if pos != "o":
                continue
            
            # Check up
            if i > 1:
                if board[i - 1][j] == "o" and board[i - 2][j] == ".":
                    nb = board.copy()
                    nb[i][j] = "."
                    nb[i - 1][j] = "."
                    nb[i - 2][j] = "o"
                    if (nbs := "".join(nb)) not in bank:
                        queue.append(nb)
                        bank[nbs] = nm + 1
            
            # Check down
            if i < 3:
                if board[i + 1][j] == "o" and board[i + 2][j] == ".":
                    nb = board.copy()
                    nb[i][j] = "."
                    nb[i + 1][j] = "."
                    nb[i + 2][j] = "o"
                    if (nbs := "".join(nb)) not in bank:
                        queue.append(nb)
                        bank.add(nbs)
            
            # Check left
            if j > 1:
                if board[i][j - 1] == "o" and board[i][j - 2] == ".":
                    nb = board.copy()
                    nb[i][j] = "."
                    nb[i][j - 1] = "."
                    nb[i][j - 2] = "o"
                    if (nbs := "".join(nb)) not in bank:
                        queue.append(nb)
                        bank.add(nbs)
            
            # Check right
            if j < 7:
                if board[i][j + 1] == "o" and board[i][j + 2] == ".":
                    nb = board.copy()
                    nb[i][j] = "."
                    nb[i][j + 1] = "."
                    nb[i][j + 2] = "o"
                    if (nbs := "".join(nb)) not in bank:
                        queue.append(nb)
                        bank.add(nbs)

# Main function
def pebbles_solitaire():
    # For each test case
    for _ in range(int(input())):
        # Get input
        board = []
        for _ in range(5):
            board.append(list(input()))

        # Reset vars
        bank = dict()
        queue = []
        score = board.count("o")

        # Compute all possible moves (at most once each)
        add_moves(board, queue, bank, 0)
        while queue:
            board = queue.pop()
            cur_board_score = board.count("o")
            add_moves(board, queue, bank)

            # Update score if needed
            if cur_board_score < score:
                score = cur_board_score

        # Output the best score found
        print(score)


# Main
if __name__ == "__main__":
    pebbles_solitaire()