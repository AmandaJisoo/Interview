import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        
        # use two pointers to solve the problem
        aPointer, bPointer = 0, 0
        character = set()
        longest = 0
        while (bPointer < len(s)):
            if s[bPointer] not in character:
                character.add(s[bPointer])
                bPointer += 1
                longest = max((len(character)), longest)
            else:
                character.remove(s[aPointer])
                aPointer += 1
        return longest



