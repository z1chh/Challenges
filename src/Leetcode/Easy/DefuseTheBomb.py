class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Initialize new array
        decrypted = []

        # Check if k is 0
        if k == 0:
            for d in code:
                decrypted.append(0)
            return decrypted

        # For positive values of k
        if k > 0:
            for d in code:
                pass

        # For negative values of k
        else:
            for d in code:
                pass

        # Return decrypted code
        return decrypted
