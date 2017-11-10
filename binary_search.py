def sorted_search(elements,target):
    if not elements or len(elements)<=0:
        return -1
    left =0
    right = len(elements)-1
    while left<right:
        middle  = (left+right+1)/2
        if elements[middle] > target:
            right = middle - 1
        else:
            left = middle +  1
    if elements[right] == target:
        return elements[right]
    return -1
elements = [1,4,5,7,8,9]
target = 7
print sorted_search(elements,target)

