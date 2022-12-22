class Solution(object):
    def removeDuplicates(self, nums):
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
        for i in dupes:
            nums.pop(i)
            nums.append(0)

        # Return number of duplicates
        return size - k

# This solution works but does not respect the O(1) space requirement
