class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Initialize new array
        decrypted = []
        size = len(code)

        # Check if k is 0
        if k == 0:
            for _ in range(size):
                decrypted.append(0)
            return decrypted

        # For positive values of k
        if k > 0:
            # Compute new number for each value
            for idx in range(size):
                # Initialize vars
                newValue = 0
                nums = 0
                cur = idx + 1

                # Get sum of next k values
                while nums < k:
                    # Reset index if necessary
                    if cur >= size:
                        cur -= size

                    # Update sum
                    newValue += code[cur]

                    # Update numbers counted and index
                    nums += 1
                    cur += 1

                # Add new value
                decrypted.append(newValue)

        # For negative values of k
        else:
            # Get absolute value of k
            k = -k
            
            # Compute new number for each value
            for idx in range(size):
                # Initialize vars
                newValue = 0
                nums = 0
                cur = idx - 1

                # Get sum of next k values
                while nums < k:
                    # Reset index if necessary
                    if cur < 0:
                        cur += size

                    # Update sum
                    newValue += code[cur]

                    # Update numbers counted and index
                    nums += 1
                    cur -= 1

                # Add new value
                decrypted.append(newValue)

        # Return decrypted code
        return decrypted
