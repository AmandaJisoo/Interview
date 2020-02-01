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
            #if the back pointer is a new character encoutnering
            #add to set and proceed the back pointer and update the distance
            if s[bPointer] not in character:
                character.add(s[bPointer])
                bPointer += 1
                longest = max((len(character)), longest)
            #if duplicate, remove the start point of the search
            #update the pointer so the begining of the word will be 
            # next word
            else:
                character.remove(s[aPointer])
                aPointer += 1
        return longest
s


