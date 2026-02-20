# '''reverse an integer number'''

# num = int(input("enter a number: "))
# rev=0
# tem=num
# while num!=0:
#     rev=rev*10+num%10
#     num//=10
# if rev == tem:
#     print("palindrome")
# else:    print("not palindrome")    


num = int(input("enter a number: "))

while num!=0:
    print(num%10)
    num//=10