#sets

# A set is a collection of unique items. It is an unordered collection, which means that the items in a set do not have a specific order. Sets are mutable, which means that you can add and remove items from a set.   
# Sets are defined using curly braces {} or the set() function.
# heterogeneous data types are allowed in sets
# Sets do not allow duplicate items. If you try to add a duplicate item to a set, it will be ignored.
# set are mutable
# Sets are unordered, which means that the items in a set do not have a specific order. This means that you cannot access items in a set using an index. You can only access items in a set by iterating over the set or by using the in keyword to check if an item is in the set.

s={1,2,1,2,3,4,5}
# print(s)
# print(type(s))
# print(len(s))

# s.add(6)  # add() method is used to add an item to a set. If the item is already in the set, it will be ignored.
# print(s)

# s.remove(1)  # remove() method is used to remove an item from a set.
# print(s)

# s.pop()  # pop() method is used to remove and return an arbitrary item from a set.
# print(s)

# s.discard(5)  # discard() method is used to remove an item from a set. 
# print(s)

# s.clear()  # clear() method is used to remove all items from a set.
# print(s)

# s.update({1,2,3})  # update() method is used to add items from another set or iterable to the set.
# print(s)

# print(dir(s))  # dir() function is used to get a list of all the attributes and methods of an object.

s2={3,4,5,6,7} 

print(s.union(s2))  # union() method is used to return a new set that contains all the items from both sets.