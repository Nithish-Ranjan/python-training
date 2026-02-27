# Selection Sort

a = [2,5,4,1,3]

for i in range(len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[j]<a[min]:
            min = j
    a[i],a[min]=a[min],a[i]
print(a)