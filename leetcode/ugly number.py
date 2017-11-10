#logn solution #iterative solution

def isUgly(num): 
    if num<=0:
        return False
    fact = [2,3,5]
   
    for i in fact:
        while num % i == 0:
            num /= i
    return num == 1

print isUgly(5)
