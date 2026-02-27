# Insertion Sort 

l = [2,4,3,1,5]

for i in range(1,len(l)):
    temp=l[i]
    j = i-1
    while j>=0 and l[j]>temp:
        l[j+1]=l[j]
        j-=1
    l[j+1]=temp
        
print(l)