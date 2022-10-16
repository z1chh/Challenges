# Adds the possible moves to the queue, if the new board has not been computed yet
def add_moves(board, queue, bank):
    # Check for possible moves in the board
    for i in range(21):
        # First pattern
        if board[i: i + 3] == ["o", "o", "-"]:
            new_board = board.copy()
            new_board[i: i + 3] = ["-", "-", "o"]
            if "".join(new_board) not in bank:
                queue.append(new_board)

        # Second pattern
        elif board[i: i + 3] == ["-", "o", "o"]:
            new_board = board.copy()
            new_board[i: i + 3] = ["o", "-", "-"]
            if "".join(new_board) not in bank:
                queue.append(new_board)


# Main function
def pebbles_solitaire():
    # For each test case
    for _ in range(int(input())):
        # Get input
        board = list(input())

        # Reset vars
        bank = {}
        queue = []
        score = board.count("o")

        # Compute all possible moves (at most once each)
        add_moves(board, queue, bank)
        while queue:
            board = queue.pop()
            cur_board_score = board.count("o")
            bank["".join(board)] = cur_board_score
            add_moves(board, queue, bank)

            # Update score if needed
            if cur_board_score < score:
                score = cur_board_score

        # Output the best score found
        print(score)


# Main
if __name__ == "__main__":
    pebbles_solitaire()
