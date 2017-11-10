def pairSum1(a, k):
    if len(a)<2:
        return
    arr.sort()
    left, right = (0, len(a)-1)
    while left<right:
        currentSum=a[left]+a[right]
        if currentSum==k:
            print a[left], a[right]
            left+=1 #or right-=1
        elif currentSum<k:
            left+=1
        else:
            right-=1


arr = [0,7,-1,4,5,3]
k = 6
pairSum1(arr,k)    
