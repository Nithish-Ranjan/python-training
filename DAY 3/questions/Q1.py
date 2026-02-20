#print positive ad negative numbers from a list 

numbers = [1, -2, 3, -4, 5]
positive=[]
negative=[]

for i in numbers:
    if i>0:
        positive.append(i)
    elif i<0:
        negative.append(i)
print("Positive Elements are :",positive)
print("Negative Elements are :",negative)