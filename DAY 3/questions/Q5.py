# check if list is sorted or not

# list=[1,2,3,4,5]
# sorted = True
# for i in range(len(list)-1):
#     if(list[i]>list[i+1]):
#         sorted=False
#         break
# if sorted:
#     print('list is sorted')
# else:
#     print('list is not sorted')    

l=[]
n=int(input("Enter number of elements in list :"))
      
for i in range(n):
    l.append(int(input("Enter element :")))
