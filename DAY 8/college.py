import csv 
# with open("abc.csv","w") as file:
#     x=csv.writer(file)
#     for i in range(1,4):
#         sr = int(input("Enter the serial number:"))
#         data = input("enter name:")
#         x.writerow([sr,data])
#     file.close()
    
file = open("abc.csv","r")
x = csv.reader(file)
for i in x:
    print(i)
file.close()