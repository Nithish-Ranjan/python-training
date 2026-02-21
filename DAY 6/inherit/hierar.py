# Hierarchical Inheritance

class A:
    def __init__(self,name):
        self.name=name
    def disp1(self):
        print("Hello, I am class A and my name is",self.name)
        
class B(A): 
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def disp2(self):
        print("Hello, I am class B and my age is",self.age)
        
class C(A):
    def __init__(self,name,gender):
        super().__init__(name)
        self.gender=gender
    def disp3(self):
        print("Hello, I am class C and my gender is",self.gender)
        
b1=B("NRj",19)
b1.disp1()
b1.disp2()
c1=C("Malli", "Male")
c1.disp1()
c1.disp3()