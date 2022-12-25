class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # Initialize vars
        size = len(nums)
        removed = 0
        vals = []

        # Remove elements that are equal to val
        for i, n in enumerate(nums):
            if n == val:
                vals.append(i)
                removed += 1

        print(vals)

        # Remove elements that are equal
        vals.reverse()
        for v in vals:
            nums.pop(v)
            nums.append(0)

        # Return number of elements left
        return size - removed
