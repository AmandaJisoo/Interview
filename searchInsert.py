class Solution(object):
    def searchInsert(self, A, target):
        if not A:
            return None
            
        n = len(A)
        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) / 2
            print(low, high, mid)
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        print(low, high, mid)
        if A[mid] < target:
            return mid + 1
        else:
            return mid