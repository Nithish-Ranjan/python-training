import pickle
file = open("xyz.dat","wb")
dic = {}
for i in range(1,5):
    key = input("enter the name:")
    course = input("enter course:")
    dic[key]=course
pickle.dump(dic,file)
file.close()

file = open("xyz.dat","rb")
dic = pickle.load(file)
print(dic)
file.close()