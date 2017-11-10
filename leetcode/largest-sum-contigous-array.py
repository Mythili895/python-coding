def maxsum(array):
    current_value = 0
    max_value = 0
    counter = 0
    temp = 0
    arr = []
    max_arr = []
    
    for i in array:
        
        current_value = current_value + i
        arr.append(i)
        #print arr
        if current_value < 0:
            arr = []
            
            counter = counter +1
            if counter == len(array):
                temp = 1
            
            current_value = 0
            
        if current_value > max_value:
            max_arr = arr
            
           
            max_value = current_value
    
    if temp == 1:
        max_value = max(array)
        max_arr = []
        max_arr.append(max_value)
    return max_value
    #return max_arr
    
#LEET CODE MAIN FUNCTION
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return maxsum(nums)
