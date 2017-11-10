def digits(number):
    #d = []
    sum = 0
    if number == 0:
        return [0]
    while(number > 0):
        #d .append(number % 10)
        sum = sum + ((number % 10) * (number % 10))
        number = number/10
        
        
    return sum
def isHappy(n):
    d = []
        
    sum = n
    while(sum != 1):
        if sum in d:
            return False
        d.append(sum)
        #print sum
        sum = digits(sum)
        if(sum == 1):
            return True 
