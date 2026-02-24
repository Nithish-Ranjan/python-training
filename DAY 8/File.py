# File handling

# write,read and append a file
# Types: Text and Binary
# open() , close() 

# Text : ASCII and Variable 
# Binary : 0 and 1


# file = open("abc.txt","r")
# print(file.readline())
# print(file.readline())
# file.close()

# file = open("abc.txt","r")
# while file != None:
#     print(file.readline())

f1 = open("obj.txt","w")
f1.write("Hello i am nrj the one who is bored all the time")
f1.close()

f = open("obj.txt","r")
print(f.readline())
f.close()
 
f1 = open("mal.txt","w")
f1.write("I AM CHITTI")
f1.close()

f1 = open("abc.txt","a")
f1.write("this is appended now!")
f1.close()