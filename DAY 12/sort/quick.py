# Quick sort

def partition(arr,low,high):
    pivot = arr[low]
    left = low
    right = high
    
    while left < right:
        while left <= high and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
        arr[low],arr[right] = arr[right],arr[low]
            
    return right

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)    
        
arr = [1,5,3,2,4,6,8,7,9]
quicksort(arr,0,len(arr)-1)
print(arr)