# #data structure
# #list
# #tuple
# #dictionary
# #set

# #LIST
# #elements are ordered
# #elements are changeable
# #allows duplicate members
# #list is defined by using square brackets []
# #list is mutable
# #list is dynamic

# list = [1, 2.12, 3.1111, '4hello', 5]
# # print(list)
# # print(type(list))
# # print(len(list))
# # print(list[0])

# # list[2] = 3.14
# # print(list)

# # #negative indexing
# # print(list[-1]) #last element
# # print(list[-2]) #second last element

# # #slicing
# # print(list[0:3]) #first three elements
# # print(list[2:]) #from index 2 to end
# # print(list[:3]) #from start to index 3 
# # print(list[-1:]) #last element to end
# # print(list[:-1]) #from start to second last element 

# list.append(6) #add element at the end of the list
# print(list)

# list.remove(2.12) #remove element by value
# print(list)

# list.pop(0) #remove element by index
# print(list)

# list.insert(0, 1) #insert element at specific index
# print(list)

# list.extend([7, 8, 9]) #add multiple elements at the end of the list
# print(list)

# print(list.count(1)) #count occurrences of an element


nums=[1, 2, 3, 4, 5]
b=nums.copy() #create a copy of the list
b[1]=10
print(nums) #original list remains unchanged
print(b) #copied list is modified