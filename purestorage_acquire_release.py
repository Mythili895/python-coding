def  check_log_history( events):
    #print (events)
    arr = []
    c = 0
    for i in events:
        c = c+1
        if i in arr:
            return c 
        if "ACQUIRE" in i:
            arr.append(i)
        event , number = i.split(' ')
        if ("RELEASE" in i) and (arr[len(arr) -1] == ("ACQUIRE " + str(number))) :
            arr.pop()
        elif ("RELEASE" in i) and (arr[len(arr) -1] != ("ACQUIRE " + str(number))):
            return c
            
            
    if arr == []:
        return 0
    else:
        return c+1
        

        return 1 
