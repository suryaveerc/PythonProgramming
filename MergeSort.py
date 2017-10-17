def mergeSort(lst):
    length = len(lst)
    if length == 1:
        return
    mid = length//2
    
    left = lst[:mid]
    right = lst[mid:]
    
    mergeSort(left)
    mergeSort(right)
    llen = mid
    rlen = length - mid
    l=r=0
    for i in range(length):
        #check if elements in right array finished or if left array still have elements and it is less than the right array element
        if r == rlen or l < llen and left[l] < right[r]: 
            lst[i]=left[l]
            l += 1
        elif l == llen or r < rlen :
            lst[i]=right[r]
            r += 1

ls = [0,2,13,3,0,1,5]
mergeSort(ls)
print(ls)