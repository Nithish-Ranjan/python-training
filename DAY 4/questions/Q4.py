#update the dictionary by adding the key of the each value in the dictionary

d1={"a":1,"b":2,"c":3}
d2={"a":4,"b":5,"c":6}
d3={}
for key in d1:
    if key in d2:
        d3[key]=d1[key]+d2[key]  # adding the value of the key in d1 and d2 and storing it in d3 with the same key
    
print(d3)