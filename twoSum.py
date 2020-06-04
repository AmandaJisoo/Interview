class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort = sorted(zip(nums, range(len(nums))))
        left, right = 0, len(sort) -1
        while left < right:
            val = sort[left][0] + sort[right][0]
            if val == target:
                return [sort[left][1], sort[right][1]]
            if val < target:
                left += 1
            else:
                right -= 1
                