class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # Initialize vars
        remainder = dividend
        quotient = 0
        neg = False

        # Remove negative numbers
        if remainder < 0:
            remainder = -remainder
            neg = True

        if divisor < 0:
            divisor = -divisor
            neg = not neg

        # Perform division
        while remainder >= divisor:
            remainder -= divisor
            quotient += 1

        # Return quotient
        return -quotient if neg else quotient
    
    # GOT TLE, PLS FIX
