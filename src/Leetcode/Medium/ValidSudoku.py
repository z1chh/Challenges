class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Check rows
        for row in board:
            digits = set()
            for d in row:
                if d != ".":
                    # Invalid if digit already exists
                    if d in digits:
                        return False

                    # Otherwise, add it to the list
                    else:
                        digits.add(d)

        # Check columns
        for col in range(9):
            digits = set()
            for row in range(9):
                # Get digit
                d = board[row][col]
                if d != ".":
                    # Invalid if digit already exists
                    if d in digits:
                        return False

                    # Otherwise, add it to the list
                    else:
                        digits.add(d)

        # Check sub-boards
        # TODO
        
        # Return True
        return True
