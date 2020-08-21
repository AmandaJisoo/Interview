
#Input: s = "3[a2[c]]"
#Output: "accaccacc"

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else: #time to upack things
                accu = ''
                while stack:
                    popped = stack.pop()
                    if popped == '[':
                        #now what I will encounter is a num and done making a chunk 
                        n = ''
                        while stack and stack[-1].isdigit():
                            n = stack.pop() + n
                        stack.append(accu * int(n))
                        break
                    else:
                        accu = popped + accu #bc the first item is in the bottom of stack
        return ''.join(stack)