class Solution(object):
    def duplicateZeros(self, arr):
        duplicate, length = 0, len(arr) -1
        #first let's count how many zeros there are
        #this will allow me to endIndex
        #Duplicate is == to the number of zeros to insert
        for i in range(len(arr)):
            if i > length - duplicate:
                break
            if arr[i] == 0:
                #if the last index is 0, then no need to make it duplicate
                #simply move over the item
                if i == length - duplicate:
                    arr[length] = 0
                    length -= 1
                    #break out if the last item
                    break
                #add count
                duplicate += 1
        lastIndex = length - duplicate
        #start from the back of the "back" of the index
        #start moving back
        #if duplicate then copy two space
        for i in range(lastIndex, -1, -1):
            if arr[i] == 0:
                arr[i + duplicate]  = 0
                arr[i + duplicate -1]  = 0
                duplicate -= 1
            else:
                arr[i + duplicate] = arr[i]
