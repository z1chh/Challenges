def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Initalize k
    size = len(nums)
    k = 0

    # Base cases
    if size < 2:
        return size

    # Get first element
    last = nums[0]

    # Remove duplicates
    dupes = []
    for i, v in enumerate(nums):
        if i == 0:
            continue
        if v == last:
            dupes.append(i - k)
            k += 1

        last = v

    # Test
    print("dupes", dupes)
    for i in dupes:
        nums.pop(i)
        nums.append(0)

    # Return number of duplicates
    print(k, nums)
    return size - k


def lengthOfLongestWord(s):
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
    if not newWord and last < length:
        last = length

    # Return the length of the last word
    return last


def main():
    #removeDuplicates([1, 1, 2])
    print(lengthOfLongestWord("Hello World Today is a magnificent day"))
    print(lengthOfLongestWord("a bb day"))


if __name__ == '__main__':
    main()
