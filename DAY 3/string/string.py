# st = '''mallu 
# loves
# bgmi 
# chicken 
# and friends'''

# print(st)

# str="hello nrj"
# # print(type(str))
# # print(len(str))
# # print(str.lower())
# # print(str.upper())
# # print(str.title())
# # print(str.capitalize())
# # print(str.swapcase())
# # print(str.count('l'))
# # print(str.find('o'))
# # print(str.index('o'))
# # print(str.replace('nrj','app'))
# # print(str.strip())
# # print(str.split())
# # print(str[::2])

# print(str.isalnum())
# print(str.isalpha())
# print(str.isdigit())
# print(str.islower())
# print(str.isupper())
# print(str.isspace())

str=input('enter a string: ')
alpha=0
number=0
space=0
special=0
for i in str:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        number+=1
    elif i.isspace():
        space+=1
    else:
        special+=1
print('alphabets:',alpha)
print('numbers:',number)    
print('spaces:',space)
print('special characters:',special)
