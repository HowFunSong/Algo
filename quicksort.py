def quicksort(arr):
    if len(arr) < 2 :
        return arr
    pivot = arr[0]
    less = [] 
    great = []
    x = 1
    while x < len(arr) :
        if arr[x] <= pivot :
            less.append(arr[x])
        elif arr[x] > pivot :
            great.append(arr[x])
        x += 1   
    return quicksort(less) + [pivot] + quicksort(great)
#實作上 pivot一定要跟 less great 分開，確保arr在recursion的過程中會越來越小，最終達到base condition 
    
unsortarr = [10,60,9,5,16,95,25]
print(quicksort(unsortarr))
