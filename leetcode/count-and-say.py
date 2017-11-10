def cnt(number):
    num = []
    val = []
    counter = 0
    new_num = []
    for i in range(len(number)):
        if i ==0:
            value = 1       
        elif number[i]!=number[i-1]:
            new_num.append(value)
            new_num.append(number[i-1])
            num.append(number[i-1])
            val.append(value)
            value = 1            
        else:            
            value = value + 1
        if i == len(number)-1:
            num.append(number[i-1])
            val.append(value)
            
            new_num.append(value)
            new_num.append(number[i])
    
    return new_num

def count(n):
    a = ""
    stra = []
    new_num = [1]
    print new_num
    
    
    for i in range(2,n+1):
        new_num = cnt(new_num)
    for i in new_num:
        a=a+str(i)
    return a
        
                
#leet code main function
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return count(n)
        
