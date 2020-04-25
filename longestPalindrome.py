class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        idea is that palindrome is a pair so 
        I will count the letters and 
        if even then I will add the pairs
        if odd, then you will add even number
        set the remainer to 1 for a key, 
        it means I can add one value in the middle
        so curLen + 1 as a middle val
        """
        if not s:
            return 0       
        dic={}
        count=0
        for i in s:
            dic[i]=dic.get(i,0)+1         
        l=list(dic.keys())
        for i in l:                          
            if dic[i]%2==0:               
                count+=dic[i]
                del(dic[i])        
            else:
                count+=dic[i]-1        
                dic[i]=1        
        if dic:return count+1       
        return count