class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        size = len(mat)
        if size == 0:
            return 0
        elif size == 1:
            return mat[0][0]
        else:
            total = 0
            for i in range(size):
                total += mat[i][i] + mat[i][size - 1 - i]
            if size % 2 == 1:
                total -= mat[size / 2][size / 2]
            return total
