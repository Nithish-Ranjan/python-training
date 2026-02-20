#find the second greatest element 

list=[5,2,3,5,1]
max=secmax= float('-inf')
for i in range(len(list)):
    if list[i]>max:
        secmax=max
        max=list[i]
    elif list[i]>secmax and list[i]!=max:
        secmax=list[i]
print("Second greatest element is :",secmax)