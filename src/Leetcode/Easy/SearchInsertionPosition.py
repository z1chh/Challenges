class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        size = len(nums)

        # Edge cases
        if size == 0:
            return 0
        if size == 1:
            return 0 if nums[0] >= target else 1
        if target < nums[0]:
            return 0

        # Initialize vars
        for i in range(size - 1):
            first = nums[i]
            second = nums[i + 1]

            # Check if target found
            if target == first:
                return i
            elif target == second:
                return i + 1

            # Check if target between first and second
            if first < target < second:
                return i + 1

        # Add at the end
        return size
