# Searching an element 
# Binary Search

arr = []
n = int(input("enter the size:"))
for i in range(n):
    m = int(input("enter the element:"))
    arr.append(m)
arr = sorted(arr)
print(arr)
left = 0
flag=0
right = len(arr) - 1
target = int(input("enter the target:"))
while left <= right:
    mid = (left+right)//2
    if arr[mid] == target:
        flag=flag+1
        break
    elif arr[mid]<target:
        left = mid+1
    else:
        right = mid-1
        
if flag == 1:
    print("element found")
else:
    print("element not found")