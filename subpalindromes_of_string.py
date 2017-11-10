def  count_palindromes( s):
    dict = {}
    for i in range(len(s)+1):
        for j in range(len(s)+1):
            t = s[i:j]
            if t == t[::-1]:
                if not dict.has_key(t):
                    dict[t] = 1
                else:
                    dict[t] = dict[t] + 1
    print dict.keys()
    c = 0
    
       
        
    for k,v in dict.items():
        
        if k != '':
            print k,v
            c = c+v
            
    return c
