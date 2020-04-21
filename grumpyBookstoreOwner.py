class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        #find people who are already happy and marked them 0
        #as they were already found
        originallySatisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0: #He's happy
                originallySatisfied += customers[i]
                customers[i] = 0
        
        # find max satisfied cutomer
        maxNumOfSatisfied = 0
        curSatisfied = 0
        for i, customersAtTime in enumerate(customers):
            curSatisfied += customersAtTime # Add current to rolling total
            if i >= X: # We need to remove some from the rolling total
                #bc I am subtracting prev possibility here when it move on to next index,
                #it is same as not adding it
                curSatisfied -= customers[i - X]
            maxNumOfSatisfied = max(maxNumOfSatisfied, curSatisfied)
        
        # The answer is the sum of the solutions for the 2 parts.
        return originallySatisfied + maxNumOfSatisfied