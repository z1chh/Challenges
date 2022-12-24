class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Reverse numbers and store in list
        n1 = [c for c in a[::-1]]
        n2 = [c for c in b[::-1]]

        # Initialize sum
        n3 = ""

        # Compute sum
        carry = False
        while n1 and n2:
            d1 = n1.pop(0)
            d2 = n2.pop(0)
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
            else:
                raise ValueError("Error: input must be binary numbers")

        # Make sure we go through each digit
        while n1:
            d = n1.pop(0)
            if d == "0" and carry:
                n3 += "1"
                carry = False
            elif d == "0":
                n3 += "0"
            elif d == "1" and carry:
                n3 += "0"
            elif d == "1":
                n3 += "1"
            else:
                raise ValueError("Error: input must be binary numbers")

        while n2:
            d = n2.pop(0)
            if d == "0" and carry:
                n3 += "1"
                carry = False
            elif d == "0":
                n3 += "0"
            elif d == "1" and carry:
                n3 += "0"
            elif d == "1":
                n3 += "1"
            else:
                raise ValueError("Error: input must be binary numbers")

        # Check for carry
        if carry:
            n3 += "1"

        # Reverse number
        n3 = n3[::-1]

        # Return sum
        return n3
