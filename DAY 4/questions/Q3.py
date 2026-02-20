# Count the frequency of each element in the dictinary

d={"a":1,"b":2,"c":3,"d":4,"e":1,"f":2}
freq={}
for key in d:
    if d[key] in freq:
        freq[d[key]]+=1
    else:
        freq[d[key]]=1   
        
print(freq)

freq={1:2,2:2,3:1,4:1}  # the output is a dictionary where the keys are the unique values from the original dictionary and the values are the count of how many times each unique value appears in the original dictionary.


