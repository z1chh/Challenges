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


def main():
    removeDuplicates([1, 1, 2])


if __name__ == '__main__':
    main()
