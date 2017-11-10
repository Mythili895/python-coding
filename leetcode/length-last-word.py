class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        t = s.split()
        if len(t) == 0:
            return 0
        size = len(t)
        return len(t[size-1])
        
