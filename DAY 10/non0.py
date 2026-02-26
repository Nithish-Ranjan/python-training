# Put all non 0 elements at last

l = [1,0,3,0,6]

for i in range(len(l)-1):
    if l[i] == 0:
        l.remove(l[i])
        l.append(0)
        
print(l)