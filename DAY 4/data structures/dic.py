#Dictionary

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their contents after they have been created.
# Dictionaries are defined using curly braces {} with key-value pairs separated by a colon :.
# heterogeneous data types are allowed in dictionaries
# Dictionaries do not allow duplicate keys. If you try to add a duplicate key to a dictionary, the new value will overwrite the existing value for that key.
# Dictionaries are unordered, which means that the items in a dictionary do not have a specific order

student = {
    "name": "nrj",
    "age": 20,
    "grade": "A"
}

# print(student)
# print(type(student))
# print(student.keys())  # keys() method is used to get a list of all the keys in a dictionary.
# print(student.values())  # values() method is used to get a list of all the values in a dictionary.
# print(student.items())  # items() method is used to get a list of all the key-value pairs in a dictionary.
# print(student)

student.update({"age": 21})  # update() method is used to update the value of a key in a dictionary.
print(student)

student["grade"] = "A+"  # you can also update the value of a key in a dictionary by using the key as an index.
print(student)

# student.pop("name")  # pop() method is used to remove a key-value pair from a dictionary and return the value of the removed key.
# print(student)

for key in student:  # you can iterate over the keys in a dictionary using a for loop.
    print(key)