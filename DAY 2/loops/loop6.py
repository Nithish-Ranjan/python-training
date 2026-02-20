'''factorial of a number'''

n = int(input('enter a number:'))
for i in range(n-1,0,-1):
    n=n*i
print('factorial=',n)