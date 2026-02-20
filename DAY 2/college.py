'''College registration system for training purposes.'''

name=input('enter your name:')
age = int (input('Enter your age: '))
marks = int(input("enter your marks:"))
att = int(input('enter your attendance percentage:'))
fee=20000
   
if (age<18 or marks<60 or att<75):
    print('you are not eligible to register')
else:
    print('you are eligible to register')
    if marks>=85 and marks<=100:
        fee=fee-(.30*fee)
    elif marks>=70:
        fee=fee-(.1*fee)
    else:
        print('No discount')
    hostel = input('are you a hosteller? Y/N :')
    hostel=hostel.upper()
    if hostel == 'Y':
        print("hostel fees is 5000.")
        fee=fee+5000
    week = input('do you want weekend classes? Y/N :')
    week = week.upper()
    if week == 'Y':
        print('weekend class cost is 2000.')
        fee=fee+2000
    if fee<15000:
        print("special approval requires")
    else:
        print('registered')
    print('Name:',name)
    print('Age:',age)
    print('Marks:',marks)
    print('Attendance:',att)
    print('Total fees:',fee)
    