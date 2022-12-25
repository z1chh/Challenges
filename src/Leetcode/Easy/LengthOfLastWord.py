class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initialize vars
        longest = 0
        cur = 0
        newWord = True

        # Iterate over every character
        for c in s:
            if newWord:
                # Check if start of a new word
                if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
                    newWord = False
                    cur = 1
            else:
                # Check if the current word ended
                if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):

                    # Check if the current word is the longest one
                    if longest < cur:
                        longest = cur

                    # Reset vars
                    newWord = True
                    cur = 0

                    # Check if the current word is the longest one
                    if longest < cur:
                        longest = cur

                # Otherwise, increment length
                else:
                    cur += 1

        # Return the length of the longest word
        return longest
