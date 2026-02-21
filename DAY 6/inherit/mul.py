# Mutiple Inheritance

class A:
    def __init__(self,name):
        self.name=name
    def disp1(self):
        print("Hello, I am class A and my name is",self.name)
        
class B:
    def __init__(self,age):
        self.age=age
    def disp2(self):
        print("Hello, I am class B and my age is",self.age)

class C(A,B):
    def __init__(self,name,age):
        A.__init__(self,name)
        B.__init__(self,age)
    def disp3(self):
        A.disp1(self)
        B.disp2(self)

c1=C("NRj",19)
c1.disp3()