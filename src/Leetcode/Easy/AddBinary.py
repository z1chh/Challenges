class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Reverse numbers
        n1 = a[::-1]
        n2 = b[::-1]

        # Initialize sum
        n3 = ""

        # Compute sum
        carry = False
        for d1, d2 in zip(n1, n2):
            if d1 == "0" and d2 == "0":
                if carry:
                    n3 += "1"
                    carry = False
                else:
                    n3 += "0"
            elif d1 == "0" and d2 == "1":
                if carry:
                    n3 += "0"
                else:
                    n3 += "1"
            elif d1 == "1" and d2 == "0":
                if carry:
                    n3 += "0"
                else:
                    n3 += "1"
            elif d1 == "1" and d2 == "1":
                if carry:
                    n3 += "1"
                else:
                    n3 += "0"
                    carry = True

        # Check for carry
        if carry:
            n3 += "1"

        # Reverse number
        n3 = n3[::-1]

        # Return sum
        return n3
