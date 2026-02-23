# ARGS and KEY ARGS

# def stud(**kw):
#     print("student info:")
#     for i in kw:
#         print(i,":",kw[i])
        
# stud(name="nrj",age=19,course="cse")

# res={i:i**2 for i in range(1,10)}
# print(res)

# l=[1,2,3,4,5,6,7,8,9,10]
# res = ["even" if i%2==0 else "odd" for i in l]
# print(res)

res = [f"even {i} : {i*i}" if i % 2 == 0 else f"odd {i}" for i in range(1, 20)]
print(res)