#mean of list of elements in list

list = [1, 2, 3, 4, 5]
# mean=sum(list)/len(list)
sum=0
for i in list:
    sum=sum+i
mean=sum/len(list)
print(mean)