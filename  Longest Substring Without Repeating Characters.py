class Solution(object):
    def lengthOfLongestSubstring(self, inputSt):
        longest = 0
        start = 0
        s = set()
        for i in range(len(inputSt)):
            if inputSt[i] in s:
                s.remove(inputSt[start])
                start += 1
            s.add(inputSt[i])
            longest = max(longest, len(s))
        return longest