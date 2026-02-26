# Put all non 0 elements at last

l = [1,0,3,0,6]
j = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i],l[j] = l[j],l[i]
        j += 1
        # l.remove(l[i])
        # l.append(0)
        
print(l)