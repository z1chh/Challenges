class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # Initalize vars
        sizeH = len(haystack)
        sizeN = len(needle)
        maxIter = sizeH - sizeN + 1

        # Check for each substring
        for i in range(maxIter):
            # If occurence found, return index
            if haystack[i: i + sizeN] == needle:
                return i

        # Otherwise, return -1
        return -1
