def decode(s):
    if len(s)==0 or s=="0" or s==" ":
        return 0
    if s[0] == '0':
        return 0 #since 0123  , 0234 is not valid , it returns 0
    score_max = [0 for x in range(len(s)+1)]
    score_max[1] = score_max[0]= 1
    for i in range(2,len(s)+1):
        score_max.append(0)
        if s[i-1] > '0':
            score_max[i] = score_max[i-1]        
        if int(s[i-2] + s[i-1]) <= 26 and int(s[i-2] + s[i-1])>=10:
            score_max[i] += score_max[i-2]
    
    return(score_max[len(s)])

#leet code main function

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return decode(s)
    
                
