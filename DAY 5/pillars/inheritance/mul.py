#multiple inheritance

class A:  #parent class or base class
    def method1(self):
        print("This is method 1 from class A")
class B:  #parent class or base class
    def method2(self):
        print("This is method 2 from class B")
        
class C(A,B):  #child class or derived class
    def method3(self):
        print("This is method 3 from class C")

c1=C()
c1.method1()
c1.method2()
c1.method3()