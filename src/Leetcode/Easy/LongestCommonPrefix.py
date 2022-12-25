class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Edge case
        if len(strs) == 0:
            return ""

        # Initialize vars
        maxLength = strs[0]

        # Get shortest string
        for s in strs:
            if curL := len(s) < maxLength:
                maxLength = curL

        # Get longest common prefix
        longest = 0
        for i in range(1, maxLength + 1):
            prefix = strs[0][0:i]
            valid = True

            # Check if every word has the same prefix
            for s in strs:
                if s[0:i] != prefix:
                    valid = False
                    break

            # Update longest common prefix, if necessary
            if valid:
                longest = i

        # Return longest common prefix
        return longest
