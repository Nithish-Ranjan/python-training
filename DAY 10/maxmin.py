l = [111111,2222,7683,12334]

min = l[0]
max = l[0]

for i in l:
    if i>max:
        max =i
    if i<min:
        min =i

print("min is:",min)
print("max is:",max)