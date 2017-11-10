#This is an recursive method to computer prime factor of a given numer

def primefactor(number , a):
    i =2
    maximum = number/2
    
    while i < maximum+1:
        if number % i == 0:
            a.append(i)
            return primefactor(number/i , a)
        i += 1
    a.append(number)
    return list(set(a))


print primefactor(2147483648,[])
