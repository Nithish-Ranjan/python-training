'''write a program take gender as input and print the salutation according to the given'''

a=(input("Enter your gender (M/F): "))
if a == 'M' or a == 'm':
    print("Good Morning, Sir!")
elif a == 'F' or a == 'f':
    print("Good Morning, Ma'am!")
else:   
    print("Invalid input. Please enter M/F.")