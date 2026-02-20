'''accept name and age from user and check they are eligible for voting or not'''
name = input("enter your name:")
age = int (input("enter yoyr age:"))
if age > 18:
    print(name,"you are eligible to vote")
else:
    print(name,"not eligible to vote")