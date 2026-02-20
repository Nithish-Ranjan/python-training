'''accept the year and check leap or not'''

year=int(input("enter the year:"))
if (year%4==0):
    if year%100==0 and year%400!=0:
        print(year,"not leap year")
    else:
        print(year,"leap year")
else:
    print(year,"not leap year")