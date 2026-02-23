# # data abstraction

class A:
    def show(self,x=None,y=None):
        if x == None and y == None:
            print("this is python programing")
        elif x != None and y == None:
            print("hello!",x)
        else:    
            print("Addition:",x+y)
            
ob = A()
ob.show()
ob.show(x=5)
ob.show(5,6)

# class B:
#     def add (self,a,b):
#         print(a+b)
        
#     def add(self,a,b,c):
#         print(a+b+c)
        
# obj=B()
# obj.add(5,10,5)

from abc import ABC,abstractmethod
class abstract(A):
    @abstractmethod
    def para(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Circle(abstract):
    def __init__(self,rad):
        self.rad=rad
        print(self.rad)
    
    def para(self):
        print(2*3.14*self.rad)
    def area(self):
        print(3.14*self.rad*self.rad)
    
        
class Square(abstract):
    def __init__(self,side):
        self.side=side
        print(self.side)
        
    def para(self):
        print(4*self.side)
    def area(self):
        print(self.side*self.side)
    
c=Circle(5)
c.para()
c.area()
s=Square(10)
s.para()
s.area() 