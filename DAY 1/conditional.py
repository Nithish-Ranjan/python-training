#conditional statements in python
# if statement
age = 18    
if age >= 18:
    print("You are an adult.")

# if-else statement
age = 16    
if age >= 18:   
    print("You are an adult.")
else:
    print("You are a minor.")   

# if-elif-else statement
age = 20    
if age < 13:    
    print("You are a child.")   
elif age < 18:    
    print("You are a teenager.")
else:
    print("You are an adult.")  
    
#nested if statement
age = 25
if age >= 18:
    if age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
else:    print("You are a minor.")  

#ternary operator
age = 30
status = "adult" if age >= 18 else "minor"
print("You are an", status) 
