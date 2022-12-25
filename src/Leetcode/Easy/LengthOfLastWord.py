class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initialize vars
        last = 0
        length = 0
        newWord = True

        # Iterate over every character
        for c in s:
            if newWord:
                # Check if start of a new word
                if c != ' ':
                    newWord = False
                    length = 1
            else:
                # Check if the current word ended
                if c == ' ':

                    # Update length of last word
                    last = length

                    # Reset vars
                    newWord = True
                    length = 0

                # Otherwise, increment length
                else:
                    length += 1

        # Check if finished with a word
        if not newWord:
            last = length

        # Return the length of the last word
        return last
