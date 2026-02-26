# Prefix Sum

l = [1,2,4,7]
print(l)
sum=0
for i in range(0,len(l)):
        sum = sum + l[i]
        l[i]=sum
        
print(l)