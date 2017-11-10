arr = [10,20,11,23,44,12]
lis = []
dict1 = {}
c = 0
for i in arr:
    lis.append(1)
    
    dict1[c] = []
    dict1[c].append(i)
    c = c +1
print lis
    
for i in range(1,len(arr)):
    print arr[i]
    for j in range(0,i):
        print arr[i] , arr[j]
        
        if arr[i]>arr[j] and lis[i]<lis[j]+1:
            dict1[i].append(arr[j])
            print arr[i] , arr[j]
            lis[i]= lis[j]+1

#print dict1[4][1:]+dict1[4][:1]
print lis        

#complete code properly