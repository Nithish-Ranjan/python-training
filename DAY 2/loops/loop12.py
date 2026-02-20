'''palindrome'''

str=input('enter a string:')
rev = ''
for i in range(len(str)-1,-1,-1):
    rev = rev + str[i]
if str == rev:
    print('palindrome')
else:
    print('not palindrome')