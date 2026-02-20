# #TUPLE
# #elements are ordered
# #elements are unchangeable
# #allows duplicate members
# #tuple is defined by using parentheses ()
# #tuple is immutable

# tuple = (1, 2, 3, 4, 5)
# print(tuple)
# print(type(tuple))
# print(len(tuple))
# print(tuple[0])
# # tuple[2] = 3.14 #this will raise an error because tuples are immutable
# # tuple.append(6) #this will also raise an error because tuples do not have an append method
# tuple.count(1) #this will work because tuples have a count method
# tuple.index(2) #this will work because tuples have an index method
# print(max(tuple)) #this will raise an error because max() cannot be used with tuples that contain different data types
# print(min(tuple)) #this will also raise an error for the same reason as max()
# t2=(1)
# print(type(t2)) #this will print <class 'int'> because t2 is not a tuple, it is just an integer
# t3=(1,) #this is a tuple with one element
# print(type(t3)) #this will print <class 'tuple'> because t3 is a


t=(1, 2, 3, 4, 5)
a,b,c,d,e=t #unpacking the tuple into variables
print(a) #1