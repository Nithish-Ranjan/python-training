#find the greatest element and print index in list

numbers = [1, 2, 3, 4, 5]
#max(numbers) #this will work because max() can be used with lists that contain different data types
max=numbers[0]
for i in numbers:
    if i>max:
        max=i
print("Greatest element is :",max)
print("Index of greatest element is :",numbers.index(max))