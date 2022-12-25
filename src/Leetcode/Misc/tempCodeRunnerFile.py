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


def lengthOfLastWord(s):
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


def main():
    #removeDuplicates([1, 1, 2])
    print(lengthOfLastWord("Hello World"))


if __name__ == '__main__':
    main()
