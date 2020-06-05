class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        writer, index = 0, 0
        while index < len(nums):
            if index == len(nums) -1 or nums[index] != nums[index + 1]:
                nums[writer] = nums[index]
                writer += 1
            index += 1
        return writer