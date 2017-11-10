def digits(number):
    d = []
    if number == 0:
        return [0]
    while(number > 0):
        d .append(number % 10)
        number = number/10
    return d



print digits(5000)        
