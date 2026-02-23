# Dunder mewthod

# these are the method which start and end with two underscore
    
class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return "hello!"
    
    def __add__(self, other):
        sum=0
        for i in other:
            sum+=i.age
        return self.age + sum
        
a = animal("nrj",15)
b = animal("mallu",20)
c = animal("malli",19)
# a.__str__()
print(a+(b,c))