class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # Initialize vars
        carry = False
        temp = []

        # Reverse list
        digits.reverse()

        # Check if overflow
        if digits[0] == 9:
            carry = True
        else:
            digits[0] += 1

        # Increment number
        for i, d in enumerate(digits):
            if d != 9:
                if carry:
                    digits[i] += 1
                    carry = False
            else:
                if carry:
                    digits[i] = 0

        # Check if overflow
        if carry:
            digits.pop()
            digits.append(0)
            digits.append(1)

        # Reverse list back to normal
        digits.reverse()

        # Return list
        return digits
