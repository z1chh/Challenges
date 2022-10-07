def add_moves(board, queue, bank):
    # Check for possible moves in the board
    for i in range(21):
        if board[i: i + 3] == ["o", "o", "-"]:
            new_board = board.copy()
            new_board[i: i + 3] = ["-", "-", "o"]
            if "".join(new_board) not in bank:
                queue.append(new_board)
        elif board[i: i + 3] == ["-", "o", "o"]:
            new_board = board.copy()
            new_board[i: i + 3] = ["o", "-", "-"]
            if "".join(new_board) not in bank:
                queue.append(new_board)

def pebbles_solitaire():
    # For each test case
    for _ in range(int(input())):
        # Get input
        board = list(input())
        
        # Reset vars
        bank = {}
        queue = []
        score = board.count("o")
        
        # 
        add_moves(board, queue, bank)
        #if not has_moves:
        #    bank["".join(game)] = game.count("o")
        while queue:
            board = queue.pop()
            cur_board_score = board.count("o")
            bank["".join(board)] = cur_board_score
            add_moves(board, queue, bank)
            
            if cur_board_score < score:
                score = cur_board_score
            
        print(score)
        
if __name__ == "__main__":
    pebbles_solitaire()