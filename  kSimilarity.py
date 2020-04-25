    def kSimilarity(self, source, target):
        visited = set()
        curr_level = {source}
        swaps = 0
        while curr_level:
            if target in curr_level:
                return swaps
            next_level = set()
            for s in curr_level:
                visited.add(s)
                #swapping so stop one index early
                for i in range(len(s) - 1):
                    #if the character at index is the same
                    #we skip
                    if s[i] == target[i]:
                        continue
                    for j in range(i + 1, len(s)):
                        #if the character at index is the same(duplicate characters)
                        #skip
                        #if  swapping does not make the target then skip
                        if s[j] == target[j] or s[j] != target[i]: 
                            continue
                        #now let's swip the characters
                        #guranteed tohave correct values until i
                        #now we swap i and j
                        #btw i and j, i + 1 and get original item btw i and j
                        #append i to original j position
                        #append the rest
                        new_s = s[:i] + s[j] + s[i + 1: j] + s[i] + s[j + 1:]
                        if new_s not in visited:
                            next_level.add(new_s)
                    break
            curr_level = next_level
            swaps += 1