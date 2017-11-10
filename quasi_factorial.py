def quasifactorial(n):
    answer = 1
    for i in range(2, n+1):
        
        answer = answer*i -1
    return answer
print quasifactorial(4)
