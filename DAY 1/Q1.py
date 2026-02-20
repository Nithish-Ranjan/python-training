'''write a program to input 2 number and print the greatest between them'''

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a > b:
    print("The greatest number is:", a) 
elif b > a:
    print("The greatest number is:", b) 
else:
    print("Both numbers are equal.")
    