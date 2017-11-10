def minsum(triangle):
    t = triangle[::-1]
    if len(triangle) == 1: return min(triangle[0])
    
    for i in range(1,len(t)):
        
        
        
        for j in range(len(t[i])):
            print t[i][j]
            t[i][j] = t[i][j] + min(t[i-1][j] , t[i-1][j+1])
            
        #print t[i] , i
        
    return t[len(t)-1][0]

#leetcode main function
class Solution(object):
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return minsum(triangle)
