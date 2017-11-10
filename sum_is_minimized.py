arr = [-1,2,5,6,1,-5,9]
arr = sorted(arr)
global left,right,mini
left = 0
right = 0
mini = 99999

def search(arr):
    
    if len(arr)>1:
        global left,right,mini
        left = arr[0]
        right = arr[len(arr)-1]
        mini = left+right
        print left,right
        if mini<0:
            #left = left+1
            search(arr[1:])
        else:
            #right = right-1
            search(arr[0:len(arr)-1])
        
    return mini
print search(arr)
            
        
        
        
    
        
    
