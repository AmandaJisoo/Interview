#two conditions: width and height
#start two pointers from the the fartest distance of width
#As we will decrement the width, to compensate the decrease of with, 
#the height should increase
#therefore move the shorter pointer, to explore potentially bigger height
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water