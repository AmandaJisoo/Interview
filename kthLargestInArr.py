class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums, 0, len(nums) -1, k)
    def quickSelect(self, nums, start, n, k):
        pos = self.partition(nums, start, n)
        if pos == k -1:# if there are k -1 number of items bigger bc indexing -1
            return nums[pos]
        elif pos >= k:# pivot is too small to be k largest
            return self.quickSelect(nums, start, pos -1, k)
        else:# pivot is too big (pos <= k)
            return self.quickSelect(nums, pos + 1, n, k)
            
        
    def partition(self, nums, left, right):
        pivot = nums[right] #last item as pivot
        i = left #tail of smaller
        for j in range(left, right):
            if nums[j] > pivot:#larger to left side of pivot
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i
        