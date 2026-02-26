l = [1,2,3,4]
print(l)

st =0
last = len(l)-1
while(st <= last):
    l[st],l[last] = l[last],l[st]
    st += 1
    last -= 1
print(l)