'''sum until n terms'''

sum=0
n = int(input('enter the number:'))
for i in range(1,n,1):
    sum=sum+i
print('sum=',sum)